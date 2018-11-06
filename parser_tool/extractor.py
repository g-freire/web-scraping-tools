#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from time import time, strftime
import json

import requests
from lxml import html

def blueprint():
    start = time()
    response = requests.get('', timeout=None) 
    e_tree = html.fromstring(response.text)  
    
    try:
        start = time()
        try:
            data1 =  "no data"       
            xpath_var = (e_tree.xpath('/text()'))[0]
            if len(xpath_var) > 0:
                data1 = xpath_var
        except:
            pass

        contract1 = { "json_key1": data1}
        print(contract1)
            
        try:
            data2 =  "no data"    
            xpath_var2 = (e_tree.xpath('/text()'))[0]  
            if len(xpath_var2) > 0:
                data2 = xpath_var2
        except:
            pass
        contract2 = {"json_key2": data2}
        print(contract2)

        
    
    except:
        raise    
    
    finally:
        print('Took ', (time()-start), 'seconds')

blueprint()