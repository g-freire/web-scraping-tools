"""
Esse script contem a implementacao para duas conhecidas bibliotecas de processamento
de html/xml. Ambas recebem os links, fazem o request e parser da pagina, extraem os
dados atraves de seletores especificos e exportam um relatorio em csv.
Implementa a pool de processos utilizando a biblioteca escolhida via argumento da linha de comando
"""
import sys
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup
from lxml import html

from helper_functions import *

ENTRADA_DADOS = 'data/10.txt'
SAIDA_DADOS = 'report-p.csv'


def main(parser_module):
    links = read_lines(ENTRADA_DADOS)
    with Pool(4) as pool:
        report = pool.map(parser_module, links)

def parse_with_lxml(file_lines):
        response = requests.get(file_lines, headers=random_headers(),timeout=15) 
        e_tree = html.fromstring(response.text)
    
        coluna_precos = []
        price = e_tree.xpath('//*[@class="skuBestPrice"]')
        preco = lxml_handler(price)
        coluna_precos.append(preco)

        coluna_nome_produtos = []
        product_name = e_tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
        nome_produto = lxml_handler(product_name)
        coluna_nome_produtos.append(nome_produto)

        coluna_titulos = []
        title = e_tree.xpath('head/title')
        titulo = lxml_handler(title)
        coluna_titulos.append(titulo)

        output_csv(SAIDA_DADOS,[coluna_precos,coluna_nome_produtos,coluna_titulos,file_lines])
        return(coluna_precos,coluna_nome_produtos,coluna_titulos)

def parse_with_bs4(file_lines):
        response = requests.get(file_lines, headers=random_headers(),timeout=15) 
        soup = BeautifulSoup(response.text, "lxml")
 
        coluna_precos = []
        price = soup.find('', class_="skuBestPrice")
        preco = bs4_handler(price)
        coluna_precos.append(preco)

        coluna_nome_produtos = []
        product_name = soup.find('',class_="product__floating-info--name")
        nome_produto = bs4_handler(product_name)
        coluna_nome_produtos.append(nome_produto)

        coluna_titulos = []
        title = soup.find('title')
        titulo = bs4_handler(title)
        coluna_titulos.append(titulo)

        output_csv(SAIDA_DADOS,[coluna_precos,coluna_nome_produtos,coluna_titulos,file_lines])
        return(coluna_precos,coluna_nome_produtos,coluna_titulos)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract-parallel.py [parser_module]")
    else:
        cmd = sys.argv[1]
        if cmd == "lxml":
            main(parse_with_lxml);
        elif cmd == "bs4":
            main(parse_with_bs4);
        else:
            print("Usage: python3 extract-parallel.py [parser_module]")
