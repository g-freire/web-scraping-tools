#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from filter_tool import *

# critical URL's that can break the algo
product_pattern = ["https://www.epocacosmeticos.com.br/some_product/p","https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p"]
duplicates = ["https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p","https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p","https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p"]
notproduct = ["https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/pr","https://www.epocacosmeticos.com.br/p"]
noturl = ['epoca/a/p', 'www.epocacosmeticos.com.br/a/p', '/www.epocacosmeticos.com.br/p', ]

def test_find_pattern_product():
    objeto = Mine('','')
    assert objeto.find_pattern_product(product_pattern) == ('https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p','https://www.epocacosmeticos.com.br/some_product/p',)
    assert objeto.find_pattern_product(duplicates) == ('https://www.epocacosmeticos.com.br/sabonete-eme-barra-dermage-secatriz/p',)
    assert objeto.find_pattern_product(notproduct) == ()
    assert objeto.find_pattern_product(noturl) == ()
    


