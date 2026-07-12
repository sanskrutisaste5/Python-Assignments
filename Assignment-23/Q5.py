#Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.

import multiprocessing
import os

def Factorial(No):
    print("Process ID :", os.getpid())
    print("Input Number :", No)

    fact = 1

    for i in range(1, No + 1):
        fact = fact * i

    return fact

def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    print("\nFactorials are:")
    print(Result)

if __name__ == "__main__":
    main()