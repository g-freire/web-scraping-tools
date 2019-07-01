import pandas as pd
import pyodbc 
from time import time, sleep
import typing
# cursor = connection.cursor()
# csv_file = open('output_bulk.csv', 'w')

# PYTHON POC OF A PI-SYSTEMS CLIENT CHUNK EXTRACTOR
# cada CSV uma tag
def extract_by_chunks(tag_name="ABC", chunk_size=3200, begin=0, end=3200):
    start = time()
    try:
        while 1:
            # adapatar para a query sytax do PI system - do atual pra tras chunksize
            # drop_the_current_table()
            pisystem_extraction_query = "SELECT * FROM  {}, INICIO {} TO {}".format(tag_name,begin, end)
            
            print(pisystem_extraction_query)
            begin = end
            end = end + chunk_size
            print("Sleeping for 3 seconds")
            sleep(3)        
            # trazer o ultimo chunk mesmo que menor que o chunk_size
            # implementar condicao de parada do loop
            # maybe do a 10% on the record count as chunk decision
            if end == 100000:
                break
            else:
                pass
            # ja está feito no VBA, funcao para ler todo o csv e escrever no formato csv
            # df.to_csv(csv_file, header=False)

    except Exception as e:print(e)

    finally:
        # csv_file.close()
        total_time = time() - start
        print('Process took', total_time, ' seconds')
        print("---------------------------------------------- ")

# PYTHON POC OF A PI-SYSTEMS CLIENT CHUNK EXTRACTOR --- BACKWARDS
def extract_by_chunks_backwards(tag_name="CDE", chunk_size=3200, begin=100000):
    start = time()
    try:
        while 1:
            # adapatar para a query sytax do PI system - do atual pra tras chunksize
            # drop_the_current_table()
            end = begin - chunk_size
            pisystem_extraction_query = "SELECT * FROM  {}, ULTIMO {} TO {}".format(tag_name,begin, end)
            print(pisystem_extraction_query)
            print("Sleeping for 3 seconds")
            sleep(3)        
            begin = end
            # trazer o ultimo chunk mesmo que menor que o chunk_size
            # implementar condicao de parada do loop
            # maybe do a 10% on the record count as chunk decision
            if end == 0:
                break
            else:
                pass
            # ja está feito no VBA, funcao para ler todo o csv e escrever no formato csv
            # df.to_csv(csv_file, header=False)

    except Exception as e:print(e)

    finally:
        # csv_file.close()
        total_time = time() - start
        print('Process took', total_time, ' seconds')
        print("---------------------------------------------- ")


if __name__ == '__main__':
    print("---------------------------------------------- ")
    print("SQLServer Chunk Extractor to CSV")
    # print('Total records on db is',get_total_rows())
    print("---------------------------------------------- ")
    # extract_load_chunk(10000)
    #implementar aqui o loop
    
    # extract_by_chunks()
    extract_by_chunks_backwards()
    
    # multiples tag loop
    # tag_list = ["ABC","CDE","EFG","HIJ","LMN","OPQ"]
    # for _ in tag_list:
    #     extract_by_chunks(tag_name=tag_list[_])


