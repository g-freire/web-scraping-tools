#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from time import time, strftime

import requests
from lxml import html

def blueprint():
    try:
        start = time()
        domain = ""      
        
        print('\033[94m', '---------------------------------------------', '\033[0m')
        print('\033[1m', 'Data extraction started at: ', strftime("%d-%m-%Y %H:%M:%S"), '\033[0m')
        print('\033[1m', 'Domain:', '\033[92m','{}'.format(domain), '\033[0m');
        
        data1 =  "no data"       
        data2 =  "no data"    
        
        try:
            response = requests.get('{}'.format(domain), timeout=None) 
            e_tree = html.fromstring(response.text)  
        except:
            pass     
       
        try:
            xpath_var = (e_tree.xpath('/text()'))[0]
            if len(xpath_var) > 0:
                data1 = xpath_var
        except:
            pass          

        try:
            xpath_var2 = (e_tree.xpath('/text()'))[0]  
            if len(xpath_var2) > 0:
                data2 = xpath_var2
        except:
            pass      

        domain_payload = {   
                            "data1": data1,
                            "data2": data2,
                         } 
        
        contract = {
                      'domain': "{}".format(domain),
                      'domain_payload': domain_payload
                   }
           
        print(contract)
        # return contract
    
    except:
        raise    
    
    finally:
            print('\033[1m','Process took: ', '\033[93m', (time() - start), '\033[0m','  seconds')
            print('\033[94m', '---------------------------------------------', '\033[0m')


blueprint()