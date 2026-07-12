#Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

import multiprocessing
import os

def SumEven(No):
    print("Process ID :", os.getpid())
    print("Input Number :", No)

    Sum = 0
    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    print("\nSum of Even Numbers:")
    print(Result)

if __name__ == "__main__":
    main()