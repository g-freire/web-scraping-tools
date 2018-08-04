import csv
from random import choice

import requests

# faz leitura e formata todas as linhas do arquivo contendo links 
def read_lines(ENTRADA_DADOS: str):
    with open (ENTRADA_DADOS, 'r') as file:
       file_links = [line.strip() for line in file]
    return file_links

# funcao para testar status HTTP de todas URL do arquivo 
def get_response(file_links):
    response = requests.get(file_links, headers=random_headers(),timeout=15) 
    return response

# exporta csv encodado corretamente para excel
def output_csv(file, content):
    with open(file, 'a', encoding='utf-8-sig') as csv_report:
        writer = csv.writer(csv_report)
        writer.writerow(content)

# funcoes para lidar com excessoes geradas por seletores vazios 
# lida com index out of range
def lxml_handler(selector):
    if len(selector) < 1:
        return ("Sem dados")
    else: 
        return (selector[0].text)
# lida com None type
def bs4_handler(selector):
    if selector is None:
        return ("Sem dados")
    else:
        return(selector.get_text()) 

# funcao para alternar diferentes agentes durante os requests
desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
                 ]

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}





