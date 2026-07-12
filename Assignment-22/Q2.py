#Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
import multiprocessing
import time
import os

def cube(No):
    print("Process is running with PID :",os.getpid())

    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    Data = [10,15,20,25]
    result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(cube,Data)

    end_time = time.perf_counter()

    print(f"Time is{end_time-start_time : .4f}")

    print(result)

if __name__ == "__main__":
    main()