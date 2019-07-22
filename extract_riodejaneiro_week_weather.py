#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lxml import html
from time import time,sleep
from datetime import datetime, timedelta
from pymongo import MongoClient


class ClimaTempoWeek:

    # parameterized constructor
    def __init__(self, id, cidade, estado):
        self.climatempo_id = id
        self.climatempo_cidade = cidade
        self.climatempo_estado = estado
        self.climatempo_icon = "https://img.ibxk.com.br/2015/05/12/12182548637388.jpg"

    def extract_week(self):

        try:

            climatempo_url_15_dias = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/{}/{}-{}".format(
                self.climatempo_id, self.climatempo_cidade, self.climatempo_estado
            )
            response = requests.get(climatempo_url_15_dias, timeout=None)
            e_tree_week_climatempo = html.fromstring(response.text)

            climatempo_array_of_when = []
            climatempo_array_of_max = []
            climatempo_array_of_min = []

            for i in range(0, 8):
                climatempo_max_xpath = "//*[@id='tempMax{}']/text()".format(i)
                climatempo_min_xpath = "//*[@id='tempMin{}']/text()".format(i)

                if len(e_tree_week_climatempo.xpath(climatempo_max_xpath)) > 0:
                    climatempo_array_of_max.append(
                        int(
                            e_tree_week_climatempo.xpath(climatempo_max_xpath)[
                                0
                            ].replace("°", "")
                        )
                    )
                else:
                    climatempo_array_of_max.append("-")
                if len(e_tree_week_climatempo.xpath(climatempo_min_xpath)) > 0:
                    climatempo_array_of_min.append(
                        int(
                            e_tree_week_climatempo.xpath(climatempo_min_xpath)[
                                0
                            ].replace("°", "")
                        )
                    )
                else:
                    climatempo_array_of_min.append("-")

            climatempo_com_contrato = {}
            climatempo_com_contrato = {
                "climatempo_collection_week_max": climatempo_array_of_max,
                "climatempo_collection_week_min": climatempo_array_of_min,
                "climacom_icon": self.climatempo_icon
            }
        except:
            pass
        return climatempo_com_contrato


class ClimaComWeek:

    # parameterized constructor
    def __init__(self, climacom_url):
        self.climacom_url = climacom_url
        self.climacom_icon = "https://img.ibxk.com.br/2015/05/12/12182548637388.jpg"

    def extract_week(self):
        try:
            response = requests.get(self.climacom_url, timeout=None)
            e_tree = html.fromstring(response.text)
        except:
            pass

        try:
            # looping the week
            array_of_when = []
            array_of_max = []
            array_of_min = []

            for i in range(1, 8):
                iterator_string = "/html/body/main/span[2]/span/span[1]/ul/li[{}]/".format(
                    i
                )
                max_xpath = iterator_string + "span[3]/span[1]/text()"
                min_xpath = iterator_string + "span[3]/span[3]/text()"
                when_xpath = iterator_string + "span[1]/span/text()"

                if len(e_tree.xpath(max_xpath)) > 0:
                    array_of_max.append(
                        int(e_tree.xpath(max_xpath)[0].replace("°", ""))
                    )
                else:
                    array_of_max.append("-")
                if len(e_tree.xpath(min_xpath)) > 0:
                    array_of_min.append(
                        int(e_tree.xpath(min_xpath)[0].replace("°", ""))
                    )
                else:
                    array_of_max.append("-")
                if len(e_tree.xpath(when_xpath)) > 0:
                    array_of_when.append(e_tree.xpath(when_xpath)[0])
                else:
                    array_of_max.append("-")

            clima_com_contrato = {
                "clima_collection_week_max": array_of_max,
                "clima_collection_week_min": array_of_min,
                "clima_collection_week_when": array_of_when,
                "climacom_icon":self.climacom_icon
            }

        except:
            pass

        return clima_com_contrato


def get_city_week_contract(city):
    # maybe persist colletion to a cloud database
    city_collection = [
        {
            "rio-de-janeiro": {
                "climatempo": [321, "riodejaneiro", "rj"],
                "climacom": ["https://www.tempo.com/rio-de-janeiro_rio-de-janeiro-l12987.htm"],
            },
            "niteroi": {
                "climatempo": [313, "niteroi", "rj"],
                "climacom": ["https://www.tempo.com/gn/3456283.htm"],
            },
            "macae": {
                "climatempo": [304, "macae", "rj"],
                "climacom": ["https://www.tempo.com/gn/3458266.htm"],
            },
        }
    ]

    if city in city_collection[0].keys():
        city_parameters =   city_collection[0][city]
        # instantiates the factory classes expanding the parameter objects arguments (w/ ctor anticorruption layer)
        climatempo_result = ClimaTempoWeek(*city_parameters['climatempo']).extract_week()
        climacom_result = ClimaComWeek(*city_parameters['climacom']).extract_week()

        result = {}
        result = {
            "cidade": city,
            "climatempo_com_contrato_week":climatempo_result,
            "clima_com_contrato_weel": climacom_result,
        }

        # PERSISTENCE - HYDRATING THE CONTRACTS
        try:
            start = time()
            time_now = datetime.now() + timedelta(hours=-3)
            result['timestamp'] = str(time_now)

            client = MongoClient('mongodb://connection_string')
            database = client["database_name"]
            collection = database[city]

            collection.drop()
            a = collection.insert_one(result)
            print("---------------------------------------------- ")
            print('Inserted contract: ', result)
            print("Obj ID:", a.inserted_id)
            print("Result:",a.acknowledged," --- ",a)
            print("Database collections:", database.list_collection_names())
            # print(result)
            sleep(3)

        except Exception as e:
            print(e)
        finally:
            total_time = time() - start
            print('Process took', total_time, ' seconds')
            print("---------------------------------------------- ")
            client.close()
            return result

if __name__ == "__main__":
    # job to batch cities extraction data
    inputs = ['niteroi','rio-de-janeiro', 'macae']
    results = [get_city_week_contract(i) for i in inputs]
    print('persisted contracts:  ', *results)


