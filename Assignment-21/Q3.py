#Design a Python application where multiple threads update a shared variable.

#Use a Lock to avoid race conditions.
#Each thread should increment the shared counter multiple times.
#Display the final value of the counter after all threads complete execution.

import threading

Counter = 0
Lock = threading.Lock()

def Display():
    global Counter

    for i in range(1000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()


def main():

    tobj1 = threading.Thread(target=Display)
    tobj2 = threading.Thread(target=Display)
    tobj3 = threading.Thread(target=Display)

    tobj1.start()
    tobj2.start()
    tobj3.start()

    tobj1.join()
    tobj2.join()
    tobj3.join()

    print("Final Counter:", Counter)

if __name__ == "__main__":
    main()