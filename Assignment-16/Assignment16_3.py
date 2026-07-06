#Write a program which contains one function named as Add() which accepts two numbers from user and returns the addition of those two numbers.

def Add(No1,No2):
    Ans = No1+No2
    return Ans

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second Number :"))

    Ret = Add(No1,No2)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()