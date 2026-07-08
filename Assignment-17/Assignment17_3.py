#Write a program which accepts one number from user and returns its factorial.

def factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact 

def main():
    No = int(input("Enter Number :"))

    Ret = factorial(No)
    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()