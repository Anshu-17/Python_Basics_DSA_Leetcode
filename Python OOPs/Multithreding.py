from threading import Thread
from time import sleep, time


def hello():
    for i in range(5):
        print("hello", i)
        sleep(0.5)


def hi():
    for i in range(5):
        print("hi", i)
        sleep(0.5)

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
sleep(0.2)
t2.start()


t1.join()
t2.join()
print("bye")