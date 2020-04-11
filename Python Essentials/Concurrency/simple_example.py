import threading
from time import sleep, time

tglobal = time()

def wait(n, id_):
    print(f"""
    FUNCTION {id_}, called at: t={int(time()-tglobal)}
    SLEEPING FOR: {n}s""")
    sleep(n)

if __name__=="__main__":
    print('threading')
    s0 = time()
    t1 = threading.Thread(target=wait, args=(2,"A"))
    t2 = threading.Thread(target=wait, args=(1,"B"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"{time()-s0}")

    print('normal')
    s1 = time()
    wait(1, "C")
    wait(2, "D")
    print(f"{time()-s1}")
