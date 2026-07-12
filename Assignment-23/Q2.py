#Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.

import multiprocessing
import os

def SumOdd(No):
    print("Process ID :", os.getpid())
    print("Input Number :", No)

    Sum = 0
    for i in range(1, No + 1, 2):
        Sum = Sum + i

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    print("\nSum of Odd Numbers:")
    print(Result)

if __name__ == "__main__":
    main()