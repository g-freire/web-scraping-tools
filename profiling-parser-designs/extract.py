"""
Esse script contem a implementacao para duas conhecidas bibliotecas de processamento
de html/xml. Ambas recebem os links, fazem o request e parser da pagina, extraem os
dados atraves de seletores especificos e exportam um relatorio em csv.
"""
import sys

import request
from bs4 import BeautifulSoup
from lxml import html

from helper_functions import *

ENTRADA_DADOS = 'data/10.txt'
SAIDA_DADOS = 'report.csv'

class Lxml:
    def __init__(self):
        pass
    
    def parse_with_lxml(self,file_links):
        for index, each_link in enumerate(file_links,start=1):
            response = requests.get(each_link, headers=random_headers(),timeout=15) 
            e_tree = html.fromstring(response.text)
        
            coluna_precos = []
            price = e_tree.xpath('//*[@class="skuBestPrice"]')
            preco = self.lxml_handler(price)
            coluna_precos.append(preco)

            coluna_nome_produtos = []
            product_name = e_tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
            nome_produto = self.lxml_handler(product_name)
            coluna_nome_produtos.append(nome_produto)

            coluna_titulos = []
            title = e_tree.xpath('head/title')
            titulo = self.lxml_handler(title)
            coluna_titulos.append(titulo)

            output_csv(SAIDA_DADOS,[index,coluna_precos,coluna_nome_produtos,each_link,coluna_titulos])
        
        return(coluna_precos,coluna_nome_produtos,coluna_titulos,each_link)
    
    def lxml_handler(self,selector):
        if len(selector) < 1:
            return ("Sem dados")
        else: 
            return (selector[0].text)

class Bs4:
    def __init__(self):
        pass
    
    def parse_with_bs4(self,file_links):
        for index, each_link in enumerate(file_links,start=1):
            response = requests.get(each_link, headers=random_headers(),timeout=15) 
            soup = BeautifulSoup(response.text, "html5lib")
    
            coluna_precos = []
            price = soup.find('', class_="skuBestPrice")
            preco = self.bs4_handler(price)
            coluna_precos.append(preco)

            coluna_nome_produtos = []
            product_name = soup.find('',class_="product__floating-info--name")
            nome_produto = self.bs4_handler(product_name)
            coluna_nome_produtos.append(nome_produto)

            coluna_titulos = []
            title = soup.find('title')
            titulo = self.bs4_handler(title)
            coluna_titulos.append(titulo)

            output_csv(SAIDA_DADOS,[index,coluna_precos,coluna_nome_produtos,each_link])
        
        return(coluna_precos,coluna_nome_produtos,coluna_titulos,each_link)
    
    def bs4_handler(self,selector):
        if selector is None:
            return ("Sem dados")
        else:
            return(selector.get_text()) 

if __name__ == "__main__":
    links = read_lines(ENTRADA_DADOS)
    if len(sys.argv) < 2:
        print("Usage: python3 extract-parallel.py [parser_module]")
    else:
        cmd = sys.argv[1]
        if cmd == "lxml":
            lxml_instance = Lxml()
            report = lxml_instance.parse_with_lxml(links)
        elif cmd == "bs4":
            bs4_instance = Bs4()
            report = bs4_instance.parse_with_bs4(links)
        else:
            print("Usage: python3 extract-parallel.py [parser_module]")


