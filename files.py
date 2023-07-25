import os
import xml.etree.ElementTree as Et
from xml.dom import minidom

j = 0
purchased_data = []
purchased_prods = []

with open('./nfce.xml', 'r', encoding='utf-8') as f:
    xml              = minidom.parse(f)
    supplier         = xml.getElementsByTagName('CNPJ')
    invoice          = xml.getElementsByTagName('cNF')
    date             = xml.getElementsByTagName('dhEmi')
    itens            = xml.getElementsByTagName('det')
    prod_code        = xml.getElementsByTagName('cProd')
    prod_bar_code    = xml.getElementsByTagName('cEAN')
    prod_description = xml.getElementsByTagName('xProd')
    prod_qtd         = xml.getElementsByTagName('qCom')
    prod_unity_value = xml.getElementsByTagName('vUnCom')
    prod_total_value = xml.getElementsByTagName('vProd')

    purchased_data.append (
        {
            'supplier': {supplier.firstChild.data},
            'invoice': {invoice.firstChild.data},
            'date': {date.firstChild.data}
        }
    )
    for i in itens:
        purchased_prods.append(
            {
                'code' : {prod_code[j].firstChild.data},
                # prod_description[j].firstChild.data,
                # prod_qtd[j].firstChild.data,
                # prod_unity_value[j].firstChild.data,
                # prod_total_value[j].firstChild.data
            },
        )
        j += 1

for i in purchased_prods:
    print(i)
