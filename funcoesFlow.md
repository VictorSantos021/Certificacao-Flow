# Contexto Tarefa
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:** `Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---

 ## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---

## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

 **Exemplo:** 

 var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN

---
 ## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---

 ## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

--- 
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---

### getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
### getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
### getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
 ## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
## novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
 ## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();
 
---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();
 
---

# Contexto Evento
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);
 
---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
## novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();

---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();

---
## getOnde

**Assinatura do método:**

getOnde()

**Retorno:**`retorna uma String com o ONDE`

`**Exemplo:**`

```
 var onde = getOnde();
 
```

**Finalidade:** Método responsável por retornar a configurção de ONDE o Evento/Listener será aplicado. O retorno é dado em caracteres, são eles: 'A' - Apontamento Automático ou Manual, 'T'-Tarefa, 'P' - Processo, 'F'-Formulário Formatado e 'E' - Embarcado.

---
## getAcao

**Assinatura do método:**

getAcao()

**Retorno:**`retorna uma String com o Ação`

`**Exemplo:**`

```
 var acao = getAcao();
 
```

**Finalidade:** Método responsável por retornar a configurção de AÇÃO o Evento/Listener será aplicado. O retorno é dado em caracteres, são eles: 'I' - Inserção, 'A' - Alteração, 'H' - Finalização, 'C' - Criação, 'D' - atribuição, 'S'- inicialização e 'E' - exclusão.

---
## getQuando

**Assinatura do método:**

getQuando()

**Retorno:**`retorna uma String com o QUANDO`

`**Exemplo:**`

```
 var quando = getQuando();
 
```

**Finalidade:** Método responsável por retornar a configurção de QUANDO o Evento/Listener será aplicado. O retorno é dado em caracteres, são eles: 'A'- Antes e 'D' - Depois

---
## getNovoDono

**Assinatura do método:**

getNovoDono()

**Retorno:**`O retorno é um código de usuário ou null quando não houver um dono`

`**Exemplo:**`

```
 var novoDono = getNovoDono();
 if(novoDono == null){
     // nesse caso a tarefa foi desatribuida.
     var donoAnterior = getDonoAnterior();
 }
 
```

**Finalidade:** Quando a ação é Atribuir/Desatribuir, essa rotina retorna a para quem a tarefa foi atribuida ou NULL quando desatribuida (use getDonoAnterior() nesse caso). O retorno é um código de usuário

---
## getDonoAnterior

**Assinatura do método:**

getDonoAnterior()

**Retorno:**`O retorno é um código de usuário ou null quando a tarefa não estava atribuída a ninguém.`

`**Exemplo:**`

```
 var novoDono = getNovoDono();
 if(novoDono == null){
     // nesse caso a tarefa foi desatribuida.
     var donoAnterior = getDonoAnterior();
 }
 
```

**Finalidade:** Quando a ação é Atribuir/Desatribuir, essa rotina retorna a quem era o dono anterior da tarefa. Normalmente NULL para atribuições (use getNovoDono() em caso de atribuição). O retorno é um código de usuário

---
## setCampo

**Assinatura do método:**

setCampo(String name, Object value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|Object|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

ctx.setCampo("DESCRPROD","Batom");

---

# QueryExecutor
Métodos disponibilizados para execução de operações **SQL**, como consultas **(SELECT)**, inserções **(INSERT)**, atualizações **(UPDATE)** e execução de **STORE PROCEDURES**.

---
## next

**Assinatura do método:**

next()

**Retorno:**`Retorna false, quando não há mais registros.`

**Finalidade:** Navega no resultado da consulta.

**Exemplo:**

 QueryExecutor query = ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE DHINCLUSAO > {DATAINCLUSAO} AND DHCONCLUSAO < {DATACONCLUSAO}");
 while(query.next())

---
## reset

**Assinatura do método:**

reset()

**Finalidade:** Descarta os parâmetros de execução.

**Exemplo:**

ctx.reset();

---
## nativeSelect

**Assinatura do método:**

nativeSelect(String query)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|query|String|A query de consulta.|

**Finalidade:** Executar a consulta. Podem ser usados parâmetros na consulta envolvendo o nome do parâmetro por chaves ("{MEU_PARAMETRO}").

**Exemplo:**

 DATAINCLUSCAO = "01/01/2020";
 ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE DHINCLUSAO > {DATAINCLUSAO} AND DHCONCLUSAO < {DATACONCLUSAO}");

---
##  update

**Assinatura do método:**

update(String query)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|query|String|Query desejada para efetuar o UPDATE ou INSERT no banco.|

**Finalidade:** Executa a query de UPDATE ou INSERT no banco. Não há retorno para esse método.

**Exemplo:**

 ctx.update("UPDATE TWFIPRN SET CODPRN = 214, CODUSUINC= 4 WHERE INDINSTPRN=2");

---
## executeProcedure

**Assinatura do método:**

executeProcedure(String name, Collection inputParam, Collection outputParamNames)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome da procedure.|
|inputParam|Collection|Coleção de parâmetros de entrada.|
|outputParamNames|Collection|Coleção de parâmetros de saída.|

**Retorno:**`Retorna uma chave e valor.`

**Finalidade:** Executa uma STORED PROCEDURE, através do nome da procedure, da coleção de parâmetros de entrada e coleção de parâmetros de saída.

**Exemplo:**

  var parametrosEntrada = {x:3, y:2, z:1 };
  var parametrosSaida= {a:1, b:2, c:3};
  ctx.executeProcedure("FLOW", parametrosEntrada, parametrosSaida);

---
## setParam

**Assinatura do método:**

setParam(String name, Object value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome do parâmetro do tipo String.|
|value|Object|Valor do parâmetro do tipo Object.|

**Finalidade:** Atribui valor aos parâmetros da consulta/alteração. Não há retorno para esse método.

**Exemplo:**

ctx.setParam("DATAINCLUSAO", "15/07/2019");

---
## close

**Assinatura do método:**

close()

**Finalidade:** Fecha a conexão e, implicitamente executa o reset().

**Exemplo:**

ctx.close();

---
## getBigDecimal

**Assinatura do método:**

getBigDecimal(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna.|

**Retorno:**`Retorna o valor da coluna.`

**Finalidade:** Retorna o valor da coluna solicitada, através do índice (1 para a 1ª coluna, 2 para a 2ª e assim por diante).

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getBigDecimal(7);

---
## getBigDecimal

**Assinatura do método:**

getBigDecimal(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna.|

**Retorno:**`Retorna o valor da coluna.`

**Finalidade:** Retorna o valor da coluna solicitada, por meio do nome da coluna no banco de dados.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getBigDecimal("CODUSUDONO");

---
## getDouble

**Assinatura do método:**

getDouble(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna.|

**Retorno:**`Retorna o valor da coluna.`

**Finalidade:** Retorna o valor da coluna solicitada, por meio do índice(1 para a 1ª coluna, 2 para a 2ª coluna e assim por diante).

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getDouble(7);

---
## getDouble

**Assinatura do método:**

getDouble(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna.|

**Retorno:**`Retorna o valor da coluna.`

**Finalidade:** Retorna o valor da coluna solicitada, através do nome da coluna no banco de dados.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getDouble("CODUSUDONO");

---
## getInt

**Assinatura do método:**

getInt(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna no SQL.|

**Retorno:**`Retorna o valor inteiro da coluna.`

**Finalidade:** Buscar o valor inteiro da coluna solicitada, atráves do índice da coluna.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getInt(7);

---
## getInt

**Assinatura do método:**

getInt(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna no SQL.|

**Retorno:**`Retorna o valor inteiro da coluna.`

**Finalidade:** Buscar o valor inteiro da coluna solicitada, por meio do nome da coluna.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getInt("CODUSUDONO");

---
## getString

**Assinatura do método:**

getString(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna no SQL.|

**Retorno:**`Retorna o valor texto de uma coluna solicitada.`

**Finalidade:** Busca o valor da coluna solicitada, através do índice (1 para a 1ª coluna, 2 para a 2ª e assim em diante).

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getString(4);

---
## getString

**Assinatura do método:**

getString(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna no SQL.|

**Retorno:**`Retorna o valor texto de uma coluna solicitada.`

**Finalidade:** Busca o valor da coluna solicitada, por meio do nome da coluna no banco de dados.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFPRN WHERE CODPRN=2");
 query.getString("NOME");

---
## getTimestamp

**Assinatura do método:**

getTimestamp(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna no SQL.|

**Retorno:**`Retorna um valor em Timestamp.`

**Finalidade:** Busca o valor da coluna solicitada, através do índice (1 para 1ª coluna, 2 para 2ª e assim em diante).

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE DHINCLUSAO > {DATAINCLUSAO} AND DHCONCLUSAO < {DATACONCLUSAO} AND INDINSTPRN=2");
 query.getTimestamp(6);

---
## getTimestamp

**Assinatura do método:**

getTimestamp(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna no SQL.|

**Retorno:**`Retorna um valor em Timestamp.`

**Finalidade:** Busca o valor da coluna solicitada, através do nome da coluna no banco de dados.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE DHINCLUSAO > {DATAINCLUSAO} AND DHCONCLUSAO < {DATACONCLUSAO} AND INDINSTPRN=2");
 query.getTimestamp("DHCONCLUSAO");

---
## getDate

**Assinatura do método:**

getDate(int col)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|col|int|Índice da coluna no SQL.|

**Retorno:**`Retorna uma data.`

**Finalidade:** Buscar o valor da coluna solicitada, através do índice (1 para a 1ª coluna, 2 para a 2ª e assim por diante).

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE INDINSTPRN=2");
 query.getDate(5);

---
## getDate

**Assinatura do método:**

getDate(String colName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|colName|String|Nome da coluna no SQL|

**Retorno:**`Retorna uma data.`

**Finalidade:** Busca o valor da coluna solicitada, por meio do nome da coluna no banco de dados.

**Exemplo:**

 query = ctx.nativeSelect("SELECT * FROM TWFIPRN WHERE INDINSTPRN=2");
 query.getDate("DHCONCLUSAO")

---
# Registro 
Operações básicas no contexto de linguagem de programação em Tarefas de Serviço: Remover, Salvar, Atualizar e Retornar.

---
## remove

**Assinatura do método:**

remove()

**Finalidade:** Remover o registro em evidência.

**Exemplo:**  

ctx.remove();

---
## save

**Assinatura do método:**

save()

**Finalidade:** Salvar as alterações do registro.

**Exemplo:**

 ctx.setCampo("DESCRPROD", descrprod);
 ctx.save();

---
## setCampo

**Assinatura do método:**

setCampo(String nome, Object valor)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo a ser alterado|
|valor|Object|Valor do campo|

**Finalidade:** Atualizar o valor do campo no Registro

**Exemplo:**  

ctx.setCampo("DESCRPROD", descrprod);

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo do Registro|

**Retorno:**`Retorna um objeto contento o valor do campo solicitado.`

**Finalidade:** Retornar o valor do campo no Registro

**Exemplo:**

ctx.getCampo("usadocomo");

---

# Eventos de Campo
Esta sessão apresenta as funções disponíveis para uso em eventos de campos (entrada, saída e alteração). Lembrando que a **ÚNICA** linguagem disponível neste contexto é Javascript.

**Observação:**

No contexto _eventos de campos_ do tipo _alteração_ também se encontram disponíveis as variáveis _**oldValue**_ (valor do campo antes da alteração) e _**newValue**_ (valor do campo após alteração).

---
## erroCampo

**Assinatura do método:**

erroCampo(String mensagem)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|mensagem|String|String (texto) contendo a mensagem que deseja apresentar no tooltip do campo.|

**Finalidade:** Sinalizar visualmente erro no campo em que o script está associado.

**Exemplo:**

Ao invocar o método erroCampo() em seu script, o campo indicará visualmente que está com erro, sendo necessário mudança nos dados para uma reavaliação.

 if (valor > 5) {
 		erroCampo("O valor do campo precisa ser maior que 5");
 }

---
## mensagemErroCampo

**Assinatura do método:**

mensagemErroCampo(String mensagem)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|mensagem|String|String (texto) contendo a mensagem que deseja apresentar ao usuário.|

**Finalidade:** Apresentar um Popup contendo uma mensagem de erro para o usuário.

**Exemplo:**

Ao invocar o método mensagemErroCampo(mensagem) em seu script, um Popup será apresentado ao usuário com a mensagem de informada no parâmetro.

 if (valor > 5) {
 erroCampo();
 		mensagemErroCampo("Para prosseguir, preencha o campo EXEMPLO com um valor menor ou igual a 5");
 }

---
## getCampo

**Assinatura do método:**

getCampo(String nomeDoCampo)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeDoCampo|String|String (texto) contendo a o nome do campo que deseja recuperar o valor.|

**Finalidade:** Recuperar o valor de um campo

**Exemplo:**

Ao invocar o método getCampo(nomeDoCampo) em seu script, o método retornará o valor presente no campo.

 var valorDoCampo = getCampo("NOME_DO_CAMPO");

---
## setCampo

**Assinatura do método:**

setCampo(String nomeDoCampo, String valor)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeDoCampo|String|String (texto) contendo a o nome do campo que deseja alterar o valor.|

**Finalidade:** Define um valor à um campo

**Exemplo:**

Ao invocar o método setCampo("NOME_DO_CAMPO","Novo valor do campo") ele receberá valor um novo valor.

 setCampo("NOME_DO_CAMPO","Novo valor do campo");

---

# Entrada do subprocesso Reutilizavel
Métodos para utilização dentro dos Dados de Entrada do Subprocesso Reutilizável.

**Métodos específicos:**

**setCampoSubProcesso:** Inserir dados no Formulário Embarcados do SubProcesso.

**novaLinhaFormatadoSubProcesso:** Insere uma nova linha no Formulário Formatado do SubProcesso. O retorno é a instância deste registro criado, com ele é possível utilizar as demais funcionalidades, por exemplo, setCampo.

**novaLinhaNativoSubProcesso:** a funcionalidade deste é igual ao novaLinhaFormatadoSubProcesso, só que ao inserir um novo registro no Fomulário Formatado, insere no Formulário Nativo.

---
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
##  getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
## novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();
 
---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();

---
##  setCampoSubProcesso

**Assinatura do método:**

setCampoSubProcesso(String nome, Object valor)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|
|valor|Object|Valor a ser inserido no campo.|

**Finalidade:** Inserir dados no Formulário Embarcados do SubProcesso.

**Exemplo:**

setCampoSubProcesso("Nome do campo", "valor");

---
## novaLinhaFormatadoSubProcesso

**Assinatura do método:**

novaLinhaFormatadoSubProcesso(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário.|

**Retorno:**`Retorna a instância da linha criada no formulário.`

**Finalidade:** Insere uma nova linha no Formulário Formatado do SubProcesso.

**Exemplo:**

var formFormatado = novaLinhaFormatadoSubProcesso("Nome do formulário");

---
## novaLinhaNativoSubProcesso

**Assinatura do método:**

novaLinhaNativoSubProcesso(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário.|

**Retorno:**`Retorna a instância da linha criada no formulário.`

**Finalidade:** Insere uma nova linha no Formulário Nativo do SubProcesso.

**Exemplo:**

var formNativo = novaLinhaNativoSubProcesso("Nome do formulário");

---
# ContextoFlowGet
Métodos para codificação em linguagem de programação no contexto de Tarefas de Serviço, que executarão automaticamente no fluxo do processo.

**Linguagens disponíveis para uso dos métodos:**

- Groovy

- Java

- JavaScript

---
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
##  getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
# ContextoSLA
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
##  getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

--- 
## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
## novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();
 
---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();

---
## getMomentoExecucao

**Assinatura do método:**

getMomentoExecucao()

**Retorno:**`retorna uma String com uma constante que representa o momento de avaliação.`

`**Exemplo:**`

```
 if(getMomentoExecucao() == 'F'){
 		//aqui seu código para contexto de avaliacao de formulários
 } if(getMomentoExecucao() == 'P'){
 		//aqui seu código para quando Instanciar processo
 } if(getMomentoExecucao() == 'CT'){
 		//aqui seu código para quando criar uma tarefa
 } if(getMomentoExecucao() == 'AT'){
 		//aqui seu código para quando atribuir/desatribuir uma tarefa a um dono
 } if(getMomentoExecucao() == 'FT'){
 		//aqui seu código para quando finalizar uma tarefa
 }
 
```

**Finalidade:** Método responsável por determinar o momento em que o SLA está sendo avaliado. O retorno é dado em caracteres, são possíveis retornos: 'CT'-Criação de tarefa, 'AT'-Atribuição/desatribuição de tarefa, 'FT'-Finalização de tarefa, 'P'-Instanciação de processo, 'F'-Persistencia de formulário.

---
## getNovoDono

**Assinatura do método:**

getNovoDono()

**Retorno:**`retorna o código do usuário ao qual a tarefa foi atribuida pra outros eventos.`

`**Exemplo:**`

```
 var novoDono = getNovoDono();
 if(novoDono == null){
     // nesse caso a tarefa foi desatribuida.
     var donoAnterior = getDonoAnterior();
 }
 
```

**Finalidade:** Quando a ação é Atribuir/Desatribuir, essa rotina retorna a para quem a tarefa foi atribuida ou NULL quando desatribuida (use getDonoAnterior() nesse caso). O retorno é um código de usuário ou null quando não houver um

---
## getDonoAnterior

**Assinatura do método:**

getDonoAnterior()

**Retorno:**`retorna o código do usuário ao qual a tarefa estava atribuida anteriormente ou NULL pra outros eventos.`

`**Exemplo:**`

```
 var novoDono = getNovoDono();
 if(novoDono == null){
     // nesse caso a tarefa foi desatribuida.
     var donoAnterior = getDonoAnterior();
 }
 
```

**Finalidade:** Quando o momento da avaliação é Atribuir/Desatribuir tarefa, essa rotina retorna a quem era o dono anterior da tarefa.

---
# Saída do Subprocesso Reutilizável
Métodos para utilização dentro dos Dados de Retorno do Subprocesso Reutilizável.

**Métodos específicos:**

**getCampoSubProcesso:** Pega os dados do Formulário Embarcado do SubProcesso.

**getLinhasFormatadoSubProcesso:** Pega os dados do Formulário Formatado do SubProcesso, o retorno é um array com as linhas preenchidas.

---
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
##  carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
## novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();

---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();

---
## getCampoSubProcesso

**Assinatura do método:**

getCampoSubProcesso(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Pegar dados do Formulário Embarcado do SubProcesso.

**Exemplo:**

var campo = getCampoSubProcesso("Nome do campo");

---
## getLinhasFormatadoSubProcesso

**Assinatura do método:**

getLinhasFormatadoSubProcesso(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário.|

**Retorno:**`Retorna um array de linhas / registros.`

**Finalidade:** Pegar dados do Formulário Formatado do SubProcesso.

**Exemplo:**

var formFormatado = getLinhasFormatadoSubProcesso("Nome do formulário");

---
# Condição de Apresentação
Esta sessão apresenta as funções disponíveis para uso no evento de Condição de Apresentação. A **ÚNICA** linguagem disponível neste contexto é Javascript.

**Observação:**

O retorno deverá ser **TRUE** ou **FALSE**.

---
## getCampo

**Assinatura do método:**

getCampo(String fieldName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome do campo.|

**Finalidade:** Pega o valor de um campo do processo.

**Exemplo:**

getCampo("ATIVO");

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Finalidade:** Pega o valor do código do processo.

**Exemplo:**

getCodProcesso();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Finalidade:** Pega o valor da Data e Hora da inclusão da tarefa no processo.

**Exemplo:**

getDhInclusao();

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Finalidade:** Pega o valor do instância do processo.

**Exemplo:**

getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Finalidade:** Pega o valor da instância da tarefa.

**Exemplo:**

getIdInstanceTarefa();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Finalidade:** Pega o código do usuário que realizou a inclusão da tarefa.

**Exemplo:**

getUsuarioInclusao();

---
## getVersao

**Assinatura do método:**

getVersao()

**Finalidade:** Pega a versão do processo.

**Exemplo:**

getVersao();

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Finalidade:** Pega o código do usuário logado.

**Exemplo:**

getUsuarioLogado();

---
##  getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String entityName)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome do formulário.|

**Finalidade:** Pega as informações dos campos do formulário.

**Exemplo:**

var formProduto = getLinhasFormulario("Produto");
var ativo = formProduto[0].ATIVO;

---
# Multiplicidade Paralela e Sequencial
É possível definir "N" execuções de uma mesma tarefa para "N" usuários e definir uma condição de parada para a mesma.

**Paralela**

Na Multiplicidade Pararela, o usuário deve definir quantas tarefas deverão ser criadas na Quantidade de Tarefas.

Nesse momento, é necessário preencher com um valor Inteiro positivo ou um Script que deverá ter um retorno com o mesmo formato.

**Para esse caso, todas as tarefas serão criadas no mesmo momento.**

Deverá ser preenchido também as Condições de parada, para este, será necessário escrever um Script que retorne um valor Booleano (True ou False), que definirá em qual momento o sistema deverá interromper a execução do processo.

Na finalização de uma das tarefas o sistema avaliará o Script e caso retorne TRUE, as demais tarefas abertas serão canceladas.

Caso retorne FALSE ou algum valor não Booleano, o sistema aguardará até a finalização de todas as tarefas para continuar.

**Sequencial**

Na Multiplicidade Sequencial, o usuário deve definir quantas tarefas deverão ser criadas na Quantidade de Tarefas.

Nesse momento, é necessário preencher com um valor Inteiro positivo ou um Script que deverá ter um retorno com o mesmo formato.

**Para esse caso, será criado uma tarefa por vez até a finalização da quantidade ou até a Condição de parada ser verdadeira.**

Deverá ser preenchido também as Condições de parada, para este, será necessário escrever um Script que retorne um valor Booleano (True ou False), que definirá em qual momento o sistema deverá interromper a execução do processo.

Na finalização das tarefas o sistema avaliará o Script e caso retorne TRUE, ele interromperá a criação da próxima tarefa e continuará o processo.

Caso retorne FALSE ou algum valor não Booleano, o sistema continuará criando as tarefas até a finalização da Quantidade de Tarefas definida.

---
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
## carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---

# Web Service Interno

É possível realizar a chamada de um serviço Sankhya a partir de uma tarefa de serviço de forma contextualizada.

Após a inserção dos parâmetros necessários para o serviço escolhido é possível capturar o retorno desta execução e utilizá-lo de diversas formas.

**Observação:**

O retorno da execução deste serviço poderá ser obtido através da utilização da variável **retornoWSI**. Com isso, é possível manipular este valor da melhor forma que decidir.

Um exemplo simples é inseri-lo dentro do campo de um formulário.

**Exemplo:**

 ctx.setCampo("NOME CAMPO", retornoWSI);

---
## getQuery

**Assinatura do método:**

getQuery()

**Retorno:**`Retorna um objeto do tipo QueryExecutor.`

**Finalidade:** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados.

**Exemplo:**

QueryExecutor query = getQuery();

---
## getParametroSistema

**Assinatura do método:**

getParametroSistema(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|O nome do parâmetro do sistema que deseja recuperar.|

**Retorno:**`Retorna um objeto contento o parâmetro de sistema que foi solicitado.`

**Finalidade:** Retorna o valor de um parâmetro qualquer do Sankhya/W.

**Exemplo:**

var parametro = getParametroSistema("UTILIZAHTML5");

---
## getUsuarioLogado

**Assinatura do método:**

getUsuarioLogado()

**Retorno:**`Retorna o ID do usuário informado no campo "Usuário Executante"`

**Finalidade:** Retorna o ID do Usuário Executante associado a alguma Tarefa de Serviço.

var idUsuario = getUsuarioLogado();

---
## getCampo

**Assinatura do método:**

getCampo(String nome)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nome|String|Nome do campo.|

**Retorno:**`Retorna o valor do campo solicitado.`

**Finalidade:** Recupera o valor de um campo solicitado por parâmetro.

**Exemplo:**

 var processo = buscarDado("CODPRN", "TWFIPRN","VERSAO=:VERSAO",[1]);
 var codigoProcesso = processo.getCampo("CODPRN");

---
## buscarDado

**Assinatura do método:**

buscarDado(String nomeCampo, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeTabela|String|Nome da tabela.|
|nomeCampo|String|Campo de uma coluna do banco de dados.|
|whereOrderGroup|String|Inserir a condição WHERE na consulta.|
|parametros|Object|Parâmetro da condição estabelecida.|

**Retorno:**`Retorna os valores de um campo de uma coluna do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **um dado** de **um registro** do banco de dados, de acordo com as cláusulas informadas, através do campo de uma coluna do banco de dados, nome da tabela, uma condição WHERE na consulta.

**Exemplo:**

var dado = buscarDado("CODPRN", "TWFIPRN", "IDINSTPN=:IDINSTPN ", [1]);

---
## buscarDados

**Assinatura do método:**

buscarDados(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeCampos|String[]|Campos da tabela do banco de dados.|
|nomeTabela|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma chave e um valor dos campos das coluna de uma tabela do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados afim de se obter **os dados das colunas** **de uma tabela** do banco de dados, de acordo com as cláusulas informadas, através das coluna de uma tabela do banco do dados, nome da tabela, e condições da consulta.

**Exemplo:**

var dados = bucarDados("CODUSUINC, CODPRN", "TWFIPRN", "IDINSTPRN = :IDINSTPRN  ORDER BY VERSAO DESC", [20]);

---
## buscarLinhas

**Assinatura do método:**

buscarLinhas(String[] nomeCampos, String nomeTabela, String whereOrderGroup, Object parametros)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|columnsName|String[]|Campos da tabela do banco de dados.|
|tableName|String|Nome da tabela.|
|whereOrderGroup|String|Condições que deseja inserir na consulta. Contudo, para inserir **ORDER BY** ou **GRUPO BY é nesserário** informar a clásula **WHERE**.|
|parametros|Object|Parâmetros das condições estabelecidas.|

**Retorno:**`Retorna uma coleção de chave e valor dos campos de uma entidade do banco de dados.`

**Finalidade:** Executa uma consulta no banco de dados a fim de se obter **vários registros/linhas** de **uma tabela** do banco de dados, por meio dos nomes das colunas do banco de dados, nome da tabela, e condições da consulta.

**Exemplo:**

var linhas = bucarLinhas("CODPRN, CODUSUDONO", "TWFPRN", "VERSAO = :VERSAO  ORDER BY NUGRUPO = :NUGRUPO", [4, 2]);

---
## getLinhasFormulario

**Assinatura do método:**

getLinhasFormulario(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do Formulário.|

**Retorno:**`Retorna um conjunto de linhas/registros.`

**Finalidade:** Retorna uma coleção de linhas/registros do formulário formatado, atráves do nome do formulário.

**Exemplo:**

var formularioCadNovoProd = getLinhasFormulario("Produto");

---
## getLinhasFormularioNativo

**Assinatura do método:**

getLinhasFormularioNativo(String nomeFormulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|nomeFormulario|String|Nome do formulário|

**Retorno:**`Retorna uma coleção de linhas do formulário nativo;`

**Finalidade:** Busca uma coleção de linhas do Formulário Nativo, atráves do nome do formulario.

**Exemplo:**

var linhas = getLinhasFormularioNativo("Produto");

---
##  carregaLinha

**Assinatura do método:**

carregaLinha(String entity, Object[] camposPK)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela.|
|camposPK|Object[]|PK do registro/linha.|

**Retorno:**`Retorna um objeto com os campos do registro/linha.`

**Finalidade:** Carrega uma linha/registro da tabela do banco de dados, através do nome da tabela, e a PK do registro/linha.

**Exemplo:**

 Object[] camposPK= {idInstanceProcesso,  idInstanceTarefa};
 registroProduto = carregaLinha("TWFITAR", camposPK);

---
## getIdInstanceProcesso

**Assinatura do método:**

getIdInstanceProcesso()

**Retorno:**`Retorna a instancia do processo.`

**Finalidade:** Busca um objeto com a instancia do processo.

**Exemplo:**

var idInstanciaProcesso = getIdInstanceProcesso();

---
## getIdInstanceTarefa

**Assinatura do método:**

getIdInstanceTarefa()

**Retorno:**`Retorna a instancia da tarefa.`

**Finalidade:** Busca um objeto com a instancia da tarefa.

**Exemplo:**

var idInstanciaTarefa = getIdInstanceTarefa();

---
## getCodProcesso

**Assinatura do método:**

getCodProcesso()

**Retorno:**`codProcesso`

**Finalidade:** Buscar o codigo do processo.

**Exemplo:**

var codProcesso = getCodProcesso();

---
## getVersao

**Assinatura do método:**

getVersao()

**Retorno:**`versao`

**Finalidade:** Buscar a versão do processo.

**Exemplo:**

var versao = getVersao();

---
## getUsuarioInclusao

**Assinatura do método:**

getUsuarioInclusao()

**Retorno:**`codUsuarioLogado`

**Finalidade:** Retornar o usuário que abriu/gerou a instância do processo.

**Exemplo:**

var usuarioInclusao = getUsuarioInclusao();

---
## getDhInclusao

**Assinatura do método:**

getDhInclusao()

**Retorno:**`Data inclusao`

**Finalidade:** Retornar a data de abertura, de geração da instância do processo.

**Exemplo:**

var dhInclusao = getDhInclusao();

---
## getIObjectInstanciaProcesso

**Assinatura do método:**

getIObjectInstanciaProcesso()

**Retorno:**`Map ObjectInstanciaProcesso`

**Finalidade:** Retornar os atributos CODPRN, VERSAO, CODUSUINC e DHINCLUSAO da instância do processo.

**Exemplo:**

var instanciaProcesso = getIObjectInstanciaProcesso();

---
## getCampos

**Assinatura do método:**

getCampos()

**Retorno:**`Retorna um conjunto de campos.`

**Finalidade:** Recuperar um conjunto de campos.

**Exemplo:**

 var processo = buscarDado("CODPRN, CODUSUINC", "TWFIPRN","INDINSTPRN=:INDINSTPRN", [12]);
 var instanciaProcesso = processo.getCampos();

---
## getEmailSolicitante

**Assinatura do método:**

getEmailSolicitante()

**Retorno:**`Email Usuário Solicitante.`

**Finalidade:** Recuperar o email do usuário solicitante.

**Exemplo:**

var email = getEmailSolicitante();

---
## eMail

**Assinatura do método:**

eMail(String titulo, String mensagem, String destinatarios)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|titulo|String|Assunto do email.|
|mensagem|String|Corpo do email.|
|destinatarios|String|Emails dos destinarios separados por vírgula.|

**Finalidade:** Disparar um e-mail dentro de uma Tarefa de Serviço, sem a necessidade de adicionar uma Tarefa de E-mail.

**Exemplo:**

eMail("Cadastro de Produto Novo", "Cadastro realizado com sucesso!", "maria@email.com,joao@email.com");

---
##  novaLinhaFormulario

**Assinatura do método:**

novaLinhaFormulario(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioFormatado = novaLinhaFormulario("Produto");

---
## novaLinhaFormularioNativo

**Assinatura do método:**

novaLinhaFormularioNativo(String formulario)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|formulario|String|Nome do formulário formatado a ser vinculado à tarefa.|

**Retorno:**`Retorna uma linha/registro`

**Finalidade:** Vincula o formulário formatado a tarefa do processo, por meio do nome do formulário.

**Exemplo:**

var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");

---
## novaLinha

**Assinatura do método:**

novaLinha(String entity)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|entity|String|Nome da tabela|

**Retorno:**`Retorna uma linha/registro.`

**Finalidade:** Insere um novo registro. Se for informado o nome da tabela do banco de dados, o registro será criado nessa tabela. Veja Bem, quando a função é chamada e o registro ainda não existe no banco de dados e esse não estará disponível em consultas até o fim da ação, contudo se durante a execução for necessário antecipar a inclusão do registro, o método **save();** do registro deve ser acionado.

**Exemplo:**

var produto = novaLinha("Produto");

---
## setCampo

**Assinatura do método:**

setCampo(String name, String value)

**Parâmetros:**

|Nome|Tipo|Descrição|
|---|---|---|
|name|String|Nome campo.|
|value|String|Valor do campo.|

**Finalidade:** Define o valor de um campo de processo.

**Exemplo:**

setCampo("DESCRPROD","Batom");

---
## salvarCamposAlterados

**Assinatura do método:**

salvarCamposAlterados()

**Finalidade:** Salvar as alterações efetuadas.

**Exemplo:**

 setCampo("DESCRPROD","Batom");
 salvarCamposAlterados();

---
## saveAll

**Assinatura do método:**

saveAll()

**Finalidade:** Salva todos os registros que estão em execução

**Exemplo:**

 var formularioNativo = novaLinhaFormularioNativo("NOME_FORMULARIO");
 formularioNativo.setCampo("nome", valor);
 saveAll();