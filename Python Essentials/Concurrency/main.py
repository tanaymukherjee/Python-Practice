import os

from math import ceil
from sodapy import Socrata
from time import time

DATA_URL = "data.cityofnewyork.us"
DATA_ID = "nc67-uf89"


if __name__ == '__main__':
    client = Socrata(DATA_URL, os.environ['APP_TOKEN'])
    results = client.get(DATA_ID, select='COUNT(*)')
    total = int(results[0]['COUNT'])
    page_size = 1000
    # num_pages = ceil(total / page_size)
    num_pages = 10

    s0 = time()
    i = 0
    while i < num_pages:
        s1 = time()
        print(f"page {i}")
        resp = client.get(DATA_ID, limit=page_size, offset=i*page_size)
        print(f"API CALL TIME: {time()-s1}")

        i += 1
        with open('output.txt', 'a+') as fh:
            for item in resp:
                fh.write(f"{str(item)}\n")

    print(f"DONE {time()-s0}")
