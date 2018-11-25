import urllib
import urllib.request
import re
from xml.dom import minidom

class Correios(object):

    PAC = 41106
    SEDEX = 40010
    SEDEX_10 = 40215
    SEDEX_HOJE = 40290
    E_SEDEX = 81019
    OTE = 44105
    NORMAL = 41017
    SEDEX_A_COBRAR = 40045

    def __init__(self):
        self.status = 'OK'

    def _getDados(self, tags_name, dom):
        dados = {}

        for tag_name in tags_name:
            try:
                dados[tag_name] = dom.getElementsByTagName(tag_name)[0]
                dados[tag_name] = dados[tag_name].childNodes[0].data
            except:
                dados[tag_name] = ''

        return dados

    def frete(self, cod='', GOCEP='08113000', HERECEP='01133000',
        peso='1', formato='2', comprimento='20', altura='10', largura='10', diametro='20',
        mao_propria='N', valor_declarado='0', aviso_recebimento='N', empresa='', senha='', toback='xml'):

        base_url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"

        fields = [
            ('nCdEmpresa', empresa),
            ('sDsSenha', senha),
            ('nCdServico', cod),
            ('sCepOrigem', HERECEP),
            ('sCepDestino', GOCEP),
            ('nVlPeso', peso),
            ('nCdFormato', formato),
            ('nVlComprimento', comprimento),
            ('nVlAltura', altura),
            ('nVlLargura', largura),
            ('nVlDiametro', diametro),
            ('sCdMaoPropria', mao_propria),
            ('nVlValorDeclarado', valor_declarado),
            ('sCdAvisoRecebimento', aviso_recebimento),
            ('StrRetorno', toback),
        ]

        url = base_url + "?" + urllib.parse.urlencode(fields)
        print(url)
        dom = minidom.parse(urllib.request.urlopen(url))
        tags_name = ('Valor', 'PrazoEntrega',)

        return { 'frete': self._getDados(tags_name, dom)['Valor'].replace(',','.'),
                 'prazo': self._getDados(tags_name, dom)['PrazoEntrega'].replace(',','.'),  }

    def cep(self, numero):
        url = 'http://cep.republicavirtual.com.br/web_cep.php?formato=xml&cep=%s' % str(numero)
        dom = minidom.parse(urllib.request.urlopen(url))

        tags_name = ('uf',
                     'cidade',
                     'bairro',
                     'tipo_logradouro',
                     'logradouro',)

        resultado = dom.getElementsByTagName('resultado')[0]
        resultado = int(resultado.childNodes[0].data)
        if resultado != 0:
            return self._getDados(tags_name, dom)
        else:
            return {}
'''
    def encomenda(self, numero):


        url = 'http://websro.correios.com.br/sro_bin/txect01$.QueryList?' \
              'P_ITEMCODE=&P_LINGUA=001&P_TESTE=&P_TIPO=001&P_COD_UNI=%s' % \
              str(numero)

        html = urllib2.urlopen(url).read()
        table = re.search(r'<table.*</TABLE>', html, re.S).group(0)

        parsed = BeautifulSoup(table)
        dados = []

        for count, tr in enumerate(parsed.table):
            if count > 4 and str(tr).strip() != '':
                if re.match(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}',
                            tr.contents[0].string):

                    dados.append({
                        'data': unicode(tr.contents[0].string),
                        'local': unicode(tr.contents[1].string),
                        'status': unicode(tr.contents[2].font.string)
                    })

                else:
                    dados[len(dados) - 1]['detalhes'] = unicode(
                        tr.contents[0].string)

        return dados

'''