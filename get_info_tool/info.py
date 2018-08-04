#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""script to gather and log information about domain owner and the tech stack """
import os
import datetime
from sys import argv

import urllib3
import certifi
import builtwith
import whois 

class Info:

    def __init__(self, url: str):
        self.url = url;
        self.date_now = datetime.datetime.now(); 
        # request and get the http response
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where());
        self.response = str(http.request('GET', url).status);
        # call reverse engineering modules
        self.reverse = builtwith.parse(url);
        self.owner = whois.whois(url);

    def print_to_CLI(self):
        print("");
        print("--------------------------------------------------------");
        print(self.date_now);
        print("--------------------------------------------------------");
        print("");
        print("URI ENDPOINT:  " + self.url );
        print("");
        print("HTTP RESPONSE STATUS:  " + self.response);
        print("");
        print("--------------------------------------------------------");
        print("TECH STACK INFO                                        *");
        print("--------------------------------------------------------");
        print(self.reverse);
        print("--------------------------------------------------------");
        print("");print("");
        print("--------------------------------------------------------");
        print("APP OWNER INFO                                         *");
        print("--------------------------------------------------------");
        print(self.owner);
        print("--------------------------------------------------------");

    def export_txt(self):
        # converting to string types
        sdate_now = str(self.date_now);
        surl = str(self.url);
        sowner = str(self.owner);
        sreverse = str(self.reverse);
        sresponse = str(self.response);
        # creating the txt file
        with open("info.txt", 'w') as out:
        # writing output to the txt file
            out.write(""); out.write(sdate_now + "\n");
            out.write("URI ENDPOINT: "+ surl + "\n");
            out.write("HTTP RESPONSE STATUS: " + sresponse + "\n");
            out.write("\n" + sowner + "\n");
            out.write("\n" + sreverse + "\n");
        
if __name__ == "__main__":
    # change the domain object to gather information from
    object_instance = Info("https://www.epocacosmeticos.com.br/")
    cli_instance = object_instance.print_to_CLI()
    export_instance = object_instance.export_txt()
    

   