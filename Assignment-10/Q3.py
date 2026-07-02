#write a program which accepts one number and prints factorial of that number
def factorial(value):

    factorial = 1
    for i in range(1,value+1):
        factorial = factorial * i
    return factorial

def main():
    value=int(input("Enter Number :"))
    Ret = factorial(value)
    print("Factorial is :",Ret)

if __name__ =="__main__":
    main()