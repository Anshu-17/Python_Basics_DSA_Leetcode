from threading import Thread
from time import time
from multiprocessing import Process

def calc(n1, n2):
    total = 0
    for n in range(n1, n2):
        total += n * n

if __name__ == "__main__":
    num = 100000000

    print("---------------Without Multithreading-------------------")
    start_time = time()
    calc(0, num)
    print(f"Time taken: {time() - start_time:.2f}")

    print("---------------Multithreading-------------------")
    t1 = Thread(target=calc, args=(0, num//2))
    t2 = Thread(target=calc, args=(num//2, num))
    start_time = time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Time taken: {time() - start_time:.2f}")

    print("---------------Multiprocessing-------------------")
    p1 = Process(target=calc, args=(0, num//2))
    p2 = Process(target=calc, args=(num//2, num))
    start_time = time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Time taken: {time() - start_time:.2f}")
