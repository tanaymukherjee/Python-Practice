import os
import threading

from math import ceil
from sodapy import Socrata
from time import time

DATA_URL = "data.cityofnewyork.us"
DATA_ID = "nc67-uf89"


def call_api(id_, page_size, offset):
    s1 = time()
    resp = client.get(id_, limit=page_size, offset=offset)
    print(f"API CALL TIME: {time()-s1}")

    with open('output.txt', 'a+') as fh:
        for item in resp:
            fh.write(f"{str(item)}\n")


if __name__ == '__main__':
    client = Socrata(DATA_URL, os.environ['APP_TOKEN'])
    results = client.get(DATA_ID, select='COUNT(*)')
    total = int(results[0]['COUNT'])
    page_size = 1000
    # num_pages = ceil(total / page_size)
    num_pages = 10

    s0 = time()
    threads = []
    for i in range(num_pages):
        t = threading.Thread(
            target=call_api,
            args=(DATA_ID, page_size, i*page_size, ),
        )
        threads.append(t)
        t.start()

    # wait for all to finish
    for th in threads:
        th.join()

    print(f"DONE {time()-s0}")
