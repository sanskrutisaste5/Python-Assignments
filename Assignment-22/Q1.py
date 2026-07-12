#Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

import multiprocessing
import time

def square(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**2)
    return sum 

def main():
    Data = [10000,20000,30000,40000]
    result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(square,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Time required : {end_time-start_time : .4f} seconds")

    print(Result)


if __name__ == "__main__":
    main()