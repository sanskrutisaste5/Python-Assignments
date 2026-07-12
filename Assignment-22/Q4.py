#Write a program to calculate 1^5 + 2^5 + ... + N^5 using Pool.map().

import multiprocessing
import time

def power(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**5)

    return sum

def main():
    Data = [1000,2000,3000,4000]

    result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(power,Data)

    end_time = time.perf_counter()

    pobj.close()
    pobj.join()

    print(f"Time required is {end_time-start_time : .4f}seconds")

    print(result)

if __name__ == "__main__":
    main()