#Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all prime numbers from that list. The main Python file accepts N numbers from the user and passes each number to the ChkPrime() function, which is part of the user-defined module named MarvellousNum. The function from the main Python file should be named ListPrime().

import MarvellousNum

def ListPrime(Arr):
    Sum = 0

    for No in Arr:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No

    return Sum

def main():
    Arr = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Arr.append(No)

    Ret = ListPrime(Arr)
    print("Addition of prime numbers:", Ret)

if __name__ == "__main__":
    main()