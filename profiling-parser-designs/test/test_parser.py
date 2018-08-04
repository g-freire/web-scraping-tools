# -*- coding: utf-8 -*-
import os

import pytest
import requests

import lxml
from lxml import html
from bs4 import BeautifulSoup


from main_functions import * 

critical_URI = [ "https://www.epocacosmeticos.com.br/bc-moisture-kick-schwarzkopf-professional-spray-condicionador/p",
                 "https://www.epocacosmeticos.com.br/flower-by-kenzo-eau-de-parfum-kenzo-perfume-feminino-refilavel/p",
                 "https://www.epocacosmeticos.com.br/brinde-hugo-boss-string-bag/p",
                 "https://www.epocacosmeticos.com.br/007-quantum-eau-de-toilette-james-bond-kit-perfume-masculino-50ml-gel-de-banho-150ml/p",
                 "https://www.epocacosmeticos.com.br/green-tea-thickening-bain-de-terre-condicionador/p",
                 "https://www.epocacosmeticos.com.br/sensual-eau-de-parfum-lomani-perfume-feminino/p",
                 "https://www.epocacosmeticos.com.br/sebium-gel-moussant-pump-bioderma-gel-de-limpeza/p",
                 "https://www.epocacosmeticos.com.br/bc-repair-recue-schwarzkopf-professional-condicionador/p"
                ]
link_com_newline = "https://www.epocacosmeticos.com.br/bc-moisture-kick-schwarzkopf-professional-spray-condicionador/p\n"
link_test = "https://www.epocacosmeticos.com.br/ck-be-eau-de-toilette-calvin-klein-perfume-unissex/p"

def test_read_lines():
   assert read_lines("data/critical.txt") == critical_URI

"""request/response tests"""
def test_get_the_response():
    assert str(get_the_responses(link_test)) == "<Response [200]>"
    assert str(get_the_responses(link_com_newline)) == "<Response [400]>"

def test_get_the_responses():
    links_criticos = read_lines("data/critical.txt")
    for each_url in links_criticos:
        assert str(get_the_responses(each_url)) == "<Response [200]>"

"""regex tests"""
def open_mock(mockfile):
    with open(mockfile, 'r') as file:
        page = file.read()
    return page

"""lxml"""
def test_regex_lxml_mock_title():
    page = open_mock('data/mock.html')
    tree = html.fromstring(page)
    title = tree.xpath('head/title')
    assert (title[0].text) == "some_title"

def test_regex_lxml_none_mock_title():
    page_none = open_mock('data/mock_none.html')
    tree_none = html.fromstring(page_none)
    title_none = tree_none.xpath('head/title')
    assert (title_none[0].text) == None

def regex_lxml_title_online(link):
   response = requests.get(link, headers=random_headers(),timeout=15) 
   e_tree = html.fromstring(response.text)
   title = e_tree.xpath('head/title')
   return (title[0].text)

def test_regex_lxml_title_online():
    assert regex_lxml_title_online(link_test) == u'Perfume Ck Be Calvin Klein Unissex - Época Cosméticos'

def test_regex_lxml_mock_name():
    page = open_mock('data/mock.html')
    tree = html.fromstring(page)
    product_name = tree.xpath('//*[@class="product_Name"]')
    assert product_name[0].text == 'some_name'

def test_regex_lxml_none_mock_name():
    page = open_mock('data/mock_none.html')
    tree = html.fromstring(page)
    product_name = tree.xpath('//*[@class="product_Name"]')
    assert product_name[0].text == None

def test_regex_lxml_from_epoca():
    page = open_mock('data/product.html')
    tree = html.fromstring(page)
    product_name = tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
    assert product_name[0].text == u'Schwarzkopf Professional Bonacure Moisture Kick - Condicionador em Spray - 200ml'

def test_regex_lxml_prod_name_online():
    response = requests.get(link_test, headers=random_headers(),timeout=15) 
    tree = html.fromstring(response.text)
    product_name = tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
    assert product_name[0].text == u"Ck Be Calvin Klein - Perfume Unissex - Eau de Toilette"

def test_regex_lxml_mock_price():
    page = open_mock('data/mock.html')
    tree = html.fromstring(page)
    product_price = tree.xpath('//*[@class="product_Price"]')
    assert product_price[0].text == '$20'

def test_regex_lxml_none_mock_price():
    page = open_mock('data/mock_none.html')
    tree = html.fromstring(page)
    product_price = tree.xpath('//*[@class="product_Price"]')
    assert (product_price[0].text) == None

def test_regex_lxml_price_from_epoca_sample():
    page = open_mock('data/product.html')
    tree = html.fromstring(page)
    product_price = tree.xpath('//*[@class="skuBestPrice"]')
    assert product_price[0].text == 'R$ 71,70'

def test_regex_lxml_prod_price_online():
    response = requests.get(link_test, headers=random_headers(),timeout=15) 
    tree = html.fromstring(response.text)
    product_price = tree.xpath('//*[@class="skuBestPrice"]')
    assert product_price[0].text == 'R$ 229,00'

""" bs4 """
def test_regex_bs4_mock_title():
    page = open_mock('data/mock.html')
    soup = BeautifulSoup(page,"lxml")
    title = soup.find('title')
    assert (title.get_text())  == "some_title"

def test_regex_bs4_mock_none_title():
    page = open_mock('data/mock_none.html')
    soup = BeautifulSoup(page,"lxml")
    title = soup.find('title')
    assert (title.get_text())  == ''

def regex_bs4_title_online(link):
    response = requests.get(link, headers=random_headers(),timeout=None) 
    soup = BeautifulSoup(response.text,"lxml")
    title = soup.find('title')
    return (title.get_text())

def test_regex_bs4_title_online():
    assert regex_bs4_title_online(link_test) == u'Perfume Ck Be Calvin Klein Unissex - Época Cosméticos'

def test_regex_bs4_mock_prod_name():
    page = open_mock('data/mock.html')
    soup = BeautifulSoup(page,"lxml")
    product_name = soup.find('',class_="product_Name")
    assert (product_name.get_text()) == 'some_name'

def test_regex_bs4_mock_prod_name():
    page = open_mock('data/mock_none.html')
    soup = BeautifulSoup(page,"lxml")
    product_name = soup.find('',class_="product_Name")
    assert (product_name.get_text()) == ''

def test_regex_bs4_prod_namefrom_epoca_sample():
    page = open_mock('data/product.html')
    soup = BeautifulSoup(page,"lxml")
    product_name = soup.find('',class_="product__floating-info--name")
    assert (product_name.get_text()) ==  u'Schwarzkopf Professional Bonacure Moisture Kick - Condicionador em Spray - 200ml'

def test_regex_bs4_title_online():
    response = requests.get(link_test, headers=random_headers(),timeout=15) 
    soup = BeautifulSoup(response.text,"lxml")
    product_name = soup.find('',class_="product__floating-info--name")
    assert (product_name.get_text()) ==  u"Ck Be Calvin Klein - Perfume Unissex - Eau de Toilette"

def test_regex_bs4_mock_prod_price():
    page = open_mock('data/mock.html')
    soup = BeautifulSoup(page,"lxml")
    product_name = soup.find('',class_="product_Price")
    assert (product_name.get_text()) == '$20'

def test_regex_bs4_mock_none_prod_price():
    page = open_mock('data/mock_none.html')
    soup = BeautifulSoup(page,"lxml")
    product_name = soup.find('',class_="product_Price")
    assert (product_name.get_text()) == ''

def test_regex_bs4_sample_prod_price():
    page = open_mock('data/product.html')
    soup = BeautifulSoup(page,"lxml")
    product_price = soup.find('', class_="skuBestPrice")
    assert (product_price.get_text()) == 'R$ 71,70'

def test_regex_bs4_prod_price_online():
    response = requests.get(link_test, headers=random_headers(),timeout=15) 
    soup = BeautifulSoup(response.text,"lxml")
    product_price = soup.find('', class_="skuBestPrice")
    assert (product_price.get_text()) ==  'R$ 229,00'

"""handlers"""
def test_lxml_handler():
    seletor_vazio = []
    assert lxml_handler(seletor_vazio) == "Sem dados"

def test_bs4_handler():
    seletor_vazio = None
    assert bs4_handler(seletor_vazio) == "Sem dados"


"""
Algumas urls do ecommerce que podem quebrar o parser:
* sem nome/preco & sem redirect (2/7500)
https://www.epocacosmeticos.com.br/bc-moisture-kick-schwarzkopf-professional-spray-condicionador/p
https://www.epocacosmeticos.com.br/flower-by-kenzo-eau-de-parfum-kenzo-perfume-feminino-refilavel/p
* sem nome/ sem preco mas com url e titulo (server redirect -> LinkNotfound)
https://www.epocacosmeticos.com.br/brinde-hugo-boss-string-bag/p -> https://www.epocacosmeticos.com.br/?ProductLinkNotFound=brinde-hugo-boss-string-bag
https://www.epocacosmeticos.com.br/007-quantum-eau-de-toilette-james-bond-kit-perfume-masculino-50ml-gel-de-banho-150ml/p -> https://www.epocacosmeticos.com.br/?ProductLinkNotFound=007-quantum-eau-de-toilette-james-bond-kit-perfume-masculino-50ml-gel-de-banho-150ml
* sem preco - mensagem "produto esgotado no momento"
https://www.epocacosmeticos.com.br/green-tea-thickening-bain-de-terre-condicionador/p
https://www.epocacosmeticos.com.br/sensual-eau-de-parfum-lomani-perfume-feminino/p
* sem preco - sem mensagem:
https://www.epocacosmeticos.com.br/sebium-gel-moussant-pump-bioderma-gel-de-limpeza/p
https://www.epocacosmeticos.com.br/bc-repair-recue-schwarzkopf-professional-condicionador/p

"""