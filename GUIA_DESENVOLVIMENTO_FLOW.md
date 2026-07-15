# Guia Definitivo: Desenvolvimento em Sankhya Flow

Este documento contém todas as regras, arquitetura, usabilidades nativas e boas práticas para desenvolvimento, edição e manutenção de fluxos BPMN do Sankhya Flow. **É de leitura obrigatória para qualquer Desenvolvedor ou IA atuando neste projeto.**

---

## 1. Regras Críticas de Edição e Exportação (Prevenção de Erros)

O Sankhya Flow utiliza o padrão **BPMN 2.0** estendido com tags próprias (`bpmnsnk:`). Falhas na manipulação do XML impedem a importação no sistema Sankhya-W.

### A. Codificação de Caracteres (O Erro Mais Comum)
- **Problema**: O Sankhya exporta os fluxos em **UTF-8 (sem BOM)**. O Windows (especialmente ferramentas nativas de console como o PowerShell) opera frequentemente em ANSI (Windows-1252) ou injeta BOM.
- **Sintoma**: Ao importar o arquivo editado para o Sankhya, caracteres como `ç`, `ã`, `é` viram caracteres bizarros (ex: `Ã§`, `Ã£`), ou a importação falha com erro de "XML Parse".
- **Regra de Ouro**: 
  - **NUNCA** use `Get-Content` / `Set-Content` do PowerShell sem forçar especificamente o UTF-8.
  - Para IAs e scripts: Use **SEMPRE** o Python (através do comando `py`) para manipular, ler e escrever nesses arquivos: `open('fluxo.bpmn', 'r', encoding='utf-8')`.
  - Para humanos: Edite os XMLs apenas em ferramentas como **VSCode** ou **Notepad++**, garantindo que o encoding no canto inferior direito esteja estritamente como **UTF-8**.

### B. Integridade Estrutural do BPMN
- O Sankhya não tolera IDs duplicados ou tags "órfãs" (ex: uma transição/seta - `sequenceFlow` - apontando para uma `UserTask` que foi deletada).
- Nunca remova atributos nativos do namespace Sankhya (ex: `xmlns:bpmnsnk="http://sankhya.com.br/bpmn"`) do cabeçalho do XML.

---

## 2. Usabilidades Nativas do Sankhya Flow (O que ele faz e como)

O Flow orquestra processos. Ele transita entre **Tarefas** através de **Eventos** e **Transições**, baseando-se em **Variáveis** (Campos).

### 2.1. Formulários Nativos (`bpmnsnk:formNativoExtension`)
Quando usamos uma Tarefa de Usuário (`UserTask`), podemos mapear os campos nativos do Sankhya (ex: tabela de Parceiros `TGFPAR` ou Serviços `TGFPRO`).
- No XML, eles aparecem como `<bpmnsnk:fieldProperty>`.
- **Atributos importantes**: 
  - `nome="AD_CATEGORIA"` (variável no fluxo / campo no banco)
  - `obrigatorio="S" ou "N"` (valida preenchimento antes de passar etapa)
  - `visivel="S" ou "N"` e `somenteLeitura="S" ou "N"`.

### 2.2. Eventos e Scripts (Javascript)
O motor do Flow roda **Javascript (Rhino)** para customizações e validações. Esses scripts ficam encapsulados na tag `<bpmnsnk:eventExtensionAttribute>`.

**Momentos de Execução (Onde a mágica acontece):**
1. **`onde="E"` (Entrada / Chegada):** O script roda no momento em que a etapa anterior terminou e o usuário está recebendo a nova tarefa na caixa de entrada. Útil para preencher valores padrão ou realizar cálculos antes de o usuário ver a tela.
2. **`onde="S"` (Saída):** O script roda quando o usuário clica em "Concluir/Avançar". Útil para validações pesadas do que o usuário preencheu (antes de seguir a seta).
3. **`onde="T"` (Transição):** Roda enquanto a "setinha" do processo está levando de uma etapa para outra. Usado para decisões ou transformações silenciosas de dados.

**Comandos Nativos do Javascript no Flow:**
- **Obter valores:** `getCampo("NOME_CAMPO")` ou uso direto como `$NOME_CAMPO` em alguns contextos. Retorna o valor atual da variável de fluxo.
- **Atribuir valores:** `setCampo("NOME_CAMPO", "Valor")`. Se for data, passe em `java.util.Date`, se número passe BigDecimal (lembre-se: é Javascript rodando em JVM!).
- **Interromper com Erro:** Se uma validação falhar, trave o processo disparando uma exceção: 
  ```javascript
  throw new Error("Atenção: A descrição precisa ter pelo menos 15 caracteres.");
  ```
- **Boas Práticas de Validação (JS):** Sempre cheque por nulo. No Sankhya, variáveis podem vir como `null`, `undefined` ou string `"null"`.
  ```javascript
  var campo = getCampo("MEU_CAMPO");
  if(campo === null || String(campo).trim() === "") { ... }
  ```

### 2.3. Decisões de Roteamento (Gateways)
- **Exclusive Gateway (XOR):** Losango com "X" ou vazio. Apenas UM caminho será seguido. Você define uma expressão na seta (`SequenceFlow`), ex: `${APROVADO == 'S'}`. A primeira que bater verdadeiro é seguida. Sempre defina um caminho "Default" (Padrão) para caso nenhuma condição bata (evita travamento do fluxo).
- **Parallel Gateway (AND):** Losango com "+". O fluxo se divide, criando múltiplas tarefas simultâneas para setores diferentes. Eles precisam se reencontrar (Merge) num outro Gateway AND para o processo seguir.

### 2.4. ServiceTasks / ScriptTasks (Tarefas de Sistema)
Usadas para rodar códigos que não devem depender de interação humana.
- **No Flow Sankhya**, geralmente usamos para acionar **Ações (Java)** customizadas (ex: integrar com banco de dados de terceiros, emitir uma nota fiscal automaticamente, atualizar tabelas paralelas).
- O motor Rhino do Javascript no Flow é restrito, logo, interações com banco de dados (`JapeSession`, `JdbcWrapper`) devem ser preferencialmente feitas em **Regras de Negócio (Java)** puras ou através de Ações mapeadas, não enchendo o XML do Flow com centenas de linhas de JS conectando em banco.

---

## 3. Diretrizes de Arquitetura de Processos

1. **Separação de Responsabilidades (O Que Fica no Flow vs. O Que Fica na Regra de Negócio/Java):**
   - **No Flow (BPMN):** Validações de UI ("preencheu o campo X?"), aprovações hierárquicas, envio de e-mails/avisos, roteamento entre departamentos.
   - **Fora do Flow (Regras Java/Sankhya na tabela):** Regras Fiscais ou Financeiras complexas, definição de TOP no faturamento baseada no cliente da nota, integrações via API (preferível Action). 
   - *Exemplo Prático:* O Cadastro de Serviço (`TGFPRO`) define a "Categoria Fiscal". Mas a TOP só é definida no momento da nota de serviço, pois depende se o *Cliente (TGFPAR)* tem alguma retenção de imposto. Portanto, a regra da TOP *não* vai no fluxo de Serviço, e sim no Sankhya (Regra na `TGFITE`).

2. **Manutenção de Logs e Variáveis:**
   - Evite criar "variáveis fantasmas" (variáveis em scripts que não existem nos formulários/tabelas). Se precisar guardar estado, crie campos AD_ (Adicionais) na tabela principal para rastreabilidade.

3. **Revisão de Código (IAs):**
   - Ao receber solicitações para alterar `.bpmn`, identifique imediatamente o `id` da tarefa (ex: `UserTask_Analise_Compras`), encontre sua extensão `<bpmnsnk:eventTaskExtension>`, extraia o Javascript, analise, altere e devolva sanitizado de volta ao fluxo usando **Python/RegEx**.
