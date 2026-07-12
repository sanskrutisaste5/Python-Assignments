#Write a program that counts how many prime numbers exist between 1 and N for every number in the given list using multiprocessing.Pool().

import multiprocessing

def PrimeCount(No):
    count = 0

    for i in range(2, No + 1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            count += 1

    return count

def main():
    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()