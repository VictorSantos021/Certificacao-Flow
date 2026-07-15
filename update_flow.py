import xml.etree.ElementTree as ET

# Registrando namespaces
ET.register_namespace('bpmn', 'http://www.omg.org/spec/BPMN/20100524/MODEL')
ET.register_namespace('bpmndi', 'http://www.omg.org/spec/BPMN/20100524/DI')
ET.register_namespace('bpmnsnk', 'http://sankhya.com.br/schema/bpmn/bpmnSnkModeler')
ET.register_namespace('dc', 'http://www.omg.org/spec/DD/20100524/DC')
ET.register_namespace('di', 'http://www.omg.org/spec/DD/20100524/DI')
ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
ET.register_namespace('camunda', 'http://camunda.org/schema/1.0/bpmn')

ns = {
    'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
    'bpmnsnk': 'http://sankhya.com.br/schema/bpmn/bpmnSnkModeler',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

tree = ET.parse('processo_1.bpmn')
root = tree.getroot()
process = root.find('bpmn:process', ns)

def add_script(task_id, script_content, onde='E'):
    task = process.find(f".//*[@id='{task_id}']", ns)
    if task is not None:
        ext = task.find('bpmn:extensionElements', ns)
        if ext is None:
            ext = ET.SubElement(task, '{http://www.omg.org/spec/BPMN/20100524/MODEL}extensionElements')
        
        # clear existing task extensions to avoid duplicates
        for existing in ext.findall('bpmnsnk:eventTaskExtension', ns):
            ext.remove(existing)

        event_task_ext = ET.SubElement(ext, '{http://sankhya.com.br/schema/bpmn/bpmnSnkModeler}eventTaskExtension')
        event_ext_attr = ET.SubElement(event_task_ext, '{http://sankhya.com.br/schema/bpmn/bpmnSnkModeler}eventExtensionAttribute')
        event_ext_attr.set('onde', onde)
        script_elem = ET.SubElement(event_ext_attr, '{http://sankhya.com.br/schema/bpmn/bpmnSnkModeler}script')
        script_elem.text = script_content

# Script 4
script_4 = """var codinstprn = getIdInstanceProcesso();
var codusuinc = buscarDado("CODUSUINC","TWFIPRN","IDINSTPRN = :IDINSTPRN", [codinstprn]);
var emailsolicitante = buscarDado("EMAIL","TSIUSU","CODUSU = :CODUSU", [codusuinc]);
setCampo("CAMEMAILSOLICITANTE", emailsolicitante);"""
add_script('UserTask_1r17f9x', script_4)

# Script 5
script_5 = """var codinstprn = getIdInstanceProcesso();
var codusuinc = buscarDado("CODUSUINC","TWFIPRN","IDINSTPRN = :IDINSTPRN", [codinstprn]);
var camContaEmpresa = getCampo("CAMCONTAEMPRESA");
var Banco = buscarDado("CODBCO","TSICTA","CODCTABCOINT = :CODCTABCOINT", [camContaEmpresa]);
var usuario = buscarDados("CODPARC, CODCENCUSPAD, CODEMP","TSIUSU","CODUSU = :CODUSU",[codusuinc]);
var parceiroSolicitante = usuario.CODPARC;
var CR = usuario.CODCENCUSPAD;
var CODEMP = usuario.CODEMP;
var camValorAdiantamento = getCampo("CAMVALORADIANTAMENTO");
var camObs = getCampo("CAMOBS");
var camDataNeg = getCampo("CAMDATANEG");
var camDataVenc = getCampo("CAMDATAVENC");
var camNatureza = getCampo("CAMNATUREZA");
var camTipoTitulo = getCampo("CAMTIPOTITULO");
var HISTORICO = camObs;
var camTOP = 1604;

var Receita = novaLinha("Financeiro");
Receita.setCampo("CODPARC",parceiroSolicitante);
Receita.setCampo("VLRDESDOB",camValorAdiantamento);
Receita.setCampo("OBSERVACAOAC",camObs);
Receita.setCampo("CODNAT",camNatureza);
Receita.setCampo("CODCTABCOINT",camContaEmpresa);
Receita.setCampo("CODTIPTIT",camTipoTitulo);
Receita.setCampo("CODTIPOPER",camTOP);
Receita.setCampo("CODCENCUS",CR);
Receita.setCampo("CODBCO",Banco);
Receita.setCampo("DTNEG",camDataNeg);
Receita.setCampo("DTVENC",camDataVenc);
Receita.setCampo("HISTORICO",HISTORICO);
Receita.setCampo("CODEMP",CODEMP);
Receita.setCampo("RECDESP",1);
Receita.setCampo("NUMNOTA",1);
Receita.save();

var Despesa = novaLinha("Financeiro");
Despesa.setCampo("CODPARC",parceiroSolicitante);
Despesa.setCampo("VLRDESDOB",camValorAdiantamento);
Despesa.setCampo("OBSERVACAOAC",camObs);
Despesa.setCampo("CODNAT",camNatureza);
Despesa.setCampo("CODCTABCOINT",camContaEmpresa);
Despesa.setCampo("CODTIPTIT",camTipoTitulo);
Despesa.setCampo("CODTIPOPER",camTOP);
Despesa.setCampo("CODCENCUS",CR);
Despesa.setCampo("CODBCO",Banco);
Despesa.setCampo("DTNEG",camDataNeg);
Despesa.setCampo("DTVENC",camDataVenc);
Despesa.setCampo("HISTORICO",HISTORICO);
Despesa.setCampo("CODEMP",CODEMP);
Despesa.setCampo("RECDESP",-1);
Despesa.setCampo("NUMNOTA",1);
Despesa.save();"""
add_script('UserTask_012euzd', script_5)

# Script 7
script_7 = """var despesas = getLinhasFormulario("AD_TWFLAND");
var codinstprn = getIdInstanceProcesso();
var codusuinc = buscarDado("CODUSUINC","TWFIPRN","IDINSTPRN = :IDINSTPRN", [codinstprn]);
var camContaEmpresa = getCampo("CAMCONTAEMPRESA");
var Banco = buscarDado("CODBCO","TSICTA","CODCTABCOINT = :CODCTABCOINT",[camContaEmpresa]);
var usuario = buscarDados("CODPARC, CODCENCUSPAD, CODEMP","TSIUSU","CODUSU = :CODUSU",[codusuinc]);
var parceiroSolicitante = usuario.CODPARC;
var CR = usuario.CODCENCUSPAD;
var CODEMP = usuario.CODEMP;
var camNatureza = getCampo("CAMNATUREZA");
var camTipoTitulo = getCampo("CAMTIPOTITULO");
var camDataNeg = getCampo("CAMDATANEG");
var camDataVenc = getCampo("CAMDATAVENC");
var HISTORICO = getCampo("CAMOBS");
var nomeparceiro = getCampo("CAMNOMEPARCEIRO");
var total = parseFloat(0);
var camTOP = 1604;
var CAMNUMNOTA = 1;

for (var i=0 ; i < despesas.length ; i ++){
  total = total + parseFloat(despesas[i].getCampo("CAMVALORDESPESA"));
}

var Financeiro = novaLinha("Financeiro");
Financeiro.setCampo("VLRDESDOB",total);
Financeiro.setCampo("NUMNOTA",CAMNUMNOTA);
Financeiro.setCampo("CODPARC",parceiroSolicitante);
Financeiro.setCampo("CODNAT",camNatureza);
Financeiro.setCampo("CODCTABCOINT",camContaEmpresa);
Financeiro.setCampo("CODTIPTIT",camTipoTitulo);
Financeiro.setCampo("CODTIPOPER",camTOP);
Financeiro.setCampo("CODCENCUS",CR);
Financeiro.setCampo("CODBCO",Banco);
Financeiro.setCampo("DTNEG",camDataNeg);
Financeiro.setCampo("DTVENC",camDataVenc);
Financeiro.setCampo("HISTORICO",HISTORICO);
Financeiro.setCampo("CODEMP",CODEMP);
Financeiro.setCampo("RECDESP",-1);
Financeiro.save();

var nufim = Financeiro.getCampo("NUFIN");

for (var i=0 ; i < despesas.length ; i ++){
  var percRateio = parseInt((parseFloat(despesas[i].getCampo("CAMVALORDESPESA")) / total)* 100);
  var codNat = despesas[i].getCampo("CODNAT");
  var Rateio = novaLinha("RateioRecDesp");
  Rateio.setCampo("NUFIN",nufim);
  Rateio.setCampo("PERCRATEIO",percRateio);
  Rateio.setCampo("CODNAT",codNat);
  Rateio.setCampo("ORIGEM","F");
  Rateio.save();
}

setCampo("CAMTOTALADIANTAMENTO",total);
setCampo("CAMNOMEPARCEIRO",nomeparceiro);"""
add_script('UserTask_0955st5', script_7)

# Script 8
script_8 = """var camIdFinanceiro = getCampo("CAMIDFINANCEIRO");
if (camIdFinanceiro !== null && camIdFinanceiro !== "NULL" && camIdFinanceiro !== "" && camIdFinanceiro !== undefined){
    var financeiro = buscarDados("RECDESP, VLRDESDOB","TGFFIN","NUFIN =:NUFIN",[camIdFinanceiro]);
    if (financeiro) {
        var camRecDesp = financeiro.RECDESP;
        var camValorDesd = financeiro.VLRDESDOB;
        var tipoFinan = "";
        if (camRecDesp == "-1") {
            tipoFinan = "Valor a ser recebido da empresa";
        } else if (camRecDesp == "1") {
            tipoFinan = "Valor a ser devolvido para empresa";
        } else {
            tipoFinan = "Valor compensado";
            camValorDesd = 0;
        }
        setCampo("CAMTIPOFINAN", tipoFinan);
        setCampo("CAMVALORDESD", camValorDesd);
    }
}"""
add_script('UserTask_126jqh5', script_8)

# Adding conditions to SequenceFlows from the Gateway
# SequenceFlow_1fvu321 (Reprovado)
seq_rep = process.find("bpmn:sequenceFlow[@id='SequenceFlow_1fvu321']", ns)
if seq_rep is not None:
    cond_expr = seq_rep.find('bpmn:conditionExpression', ns)
    if cond_expr is None:
        cond_expr = ET.SubElement(seq_rep, '{http://www.omg.org/spec/BPMN/20100524/MODEL}conditionExpression')
    cond_expr.set('{http://www.w3.org/2001/XMLSchema-instance}type', 'bpmn:tFormalExpression')
    cond_expr.text = "${CAMAPROVACAO == 'N'}"

# SequenceFlow_0zmwaad (Aprovado)
seq_apro = process.find("bpmn:sequenceFlow[@id='SequenceFlow_0zmwaad']", ns)
if seq_apro is not None:
    cond_expr = seq_apro.find('bpmn:conditionExpression', ns)
    if cond_expr is None:
        cond_expr = ET.SubElement(seq_apro, '{http://www.omg.org/spec/BPMN/20100524/MODEL}conditionExpression')
    cond_expr.set('{http://www.w3.org/2001/XMLSchema-instance}type', 'bpmn:tFormalExpression')
    cond_expr.text = "${CAMAPROVACAO == 'S'}"

with open('processo_1.bpmn', 'wb') as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    tree.write(f, encoding='utf-8')

print('Process successfully updated!')
