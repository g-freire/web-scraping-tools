#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import pytest
import requests
import lxml
from lxml import html

from helper_functions import * 
from parser import *

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

def test_get_responses():
    assert str(get_responses(link_test)) == "<Response [200]>"
    assert str(get_responses(link_com_newline)) == "<Response [400]>"

def test_get_the_responses():
    links_criticos = read_lines("data/critical.txt")
    for each_url in links_criticos:
        assert str(get_responses(each_url)) == "<Response [200]>"

def open_mock(mockfile):
    with open(mockfile, 'r') as file:
        page = file.read()
    return page

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

def test_regex_lxml_title_online():
    response = requests.get(link_test, headers=random_headers(),timeout=15) 
    tree = html.fromstring(response.text)
    product_name = tree.xpath('//*[@class="product__floating-info--name"]/h1/div')
    assert product_name[0].text == u"Ck Be Calvin Klein - Perfume Unissex - Eau de Toilette"

def test_lxml_handler():
    array_vazio = []
    assert lxml_handler(array_vazio) == "Sem dados"

