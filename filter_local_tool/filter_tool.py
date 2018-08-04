#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script para minerar os dados gerados por crawlers em .txt
1) cria objeto para ler todos os links do arquivo original
2) aplica filtro para links com padrao de url de produto
3) exporta e mostra quantidade de links do arquivo minerado (log)
"""

import re
import sys
import glob

CRAWLED_LINKS = "crawled_urls.txt"
CLEAN_OUTPUT = "filtered_urls.txt"

class Mine:

    def __init__(self,entrada, saida):
        self.entrada = entrada;
        self.saida = saida;
        
    def read_lines(self):
        with open(self.entrada, 'r') as f:
            lines = f.readlines()
        return lines

    def count_lines(self,lines):
        total_lines = len(lines)
        print("N˚ linhas em {}: {} ".format(self.entrada, total_lines))
    
    def find_pattern_product(self,links):
        """ Busca e exporta apenas urls com o padrao para produto do ecommerce
            arg: lista contendo todas as URLs do crawler
            return: tupla filtrada e sem entradas duplicadas
        """
        pattern = "https://www.epocacosmeticos.com.br\/.+\/[p]$"
        mined_list = [each_line for each_line in links if re.findall(pattern, each_line)]       
    
        remove_repetidos = set(mined_list)
        mined_tuple = tuple(remove_repetidos)
        return mined_tuple

    def export_files (self,mined_tuple):
        with open(self.saida,'w') as out:
            for each_link in mined_tuple:
                out.writelines(each_link)
          
if __name__ == "__main__":
    # log linhas do arquivo original
    instancia = Mine(CRAWLED_LINKS,CLEAN_OUTPUT)
    objeto_linhas = instancia.read_lines()
    contar_linhas = instancia.count_lines(objeto_linhas)
    # filtro
    regex = instancia.find_pattern_product(objeto_linhas)  
    exporta = instancia.export_files(regex)    
    # log linhas da saida mineirada
    objeto = Mine(CLEAN_OUTPUT, "")
    objeto_linhas = objeto.read_lines()
    contar_linhas_cleaned = objeto.count_lines(objeto_linhas)

