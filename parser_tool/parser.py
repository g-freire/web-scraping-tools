#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esse script faz leitura dos links, o request e parser da pagina, extrae os
dados atraves de seletores especificos e exporta um relatorio em csv.
"""
from multiprocessing import Pool

from lxml import html

from helper_functions import *

ENTRADA_DADOS = 'data/8804.txt'
SAIDA_DADOS = 'data/report-p.csv'

def main(core):
    """ implementa pool de processos paralelos com
        map do metodo parser e URLs
        """
    links = read_lines(ENTRADA_DADOS)
    with Pool(core) as pool:
        report = pool.map(parse_with_lxml, links)

def parse_with_lxml(links):
    """ define os seletores e callbacks do parser 
        """
    response = requests.get(links, headers=random_headers(),timeout=None) 
    e_tree = html.fromstring(response.text)

    coluna_nome_produtos = []
    product_name = e_tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
    nome_produto = lxml_handler(product_name)
    coluna_nome_produtos.append(nome_produto)

    coluna_titulos = []
    title = e_tree.xpath('head/title')
    titulo = lxml_handler(title)
    coluna_titulos.append(titulo)

    output_csv(SAIDA_DADOS,[coluna_nome_produtos,coluna_titulos,links])
    return(coluna_nome_produtos,coluna_titulos)

if __name__ == "__main__":  
    main(4)

