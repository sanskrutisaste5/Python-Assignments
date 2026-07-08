#Design a Python application that creates two threads named Prime and NonPrime.

#Both threads should accept a list of integers.
#The Prime thread should display all prime numbers from the list.
#The NonPrime thread should display all non-prime numbers from the list.

import threading

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Arr):
    print("Prime Numbers:")
    for No in Arr:
        if ChkPrime(No):
            print(No)


def NonPrime(Arr):
    print("Non Prime Numbers:")
    for No in Arr:
        if ChkPrime(No) == False:
            print(No)


def main():
    Arr = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Arr.append(No)

    tobj1 = threading.Thread(target=Prime, args=(Arr,))
    tobj2 = threading.Thread(target=NonPrime, args=(Arr,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

if __name__ == "__main__":
    main()