#write a program which accepts two numbers and prints addition , subtraction, multiplication and division

def Addition(No1,No2):
    Ans = No1+No2
    return Ans

def Subtraction(No1,No2):
    Ans = No1-No2
    return Ans

def Multiplication(No1,No2):
    Ans = No1*No2
    return Ans

def Division(No1,No2):
    Ans = No1/No2
    return Ans

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))

    Ret = Addition(No1,No2)
    print("Addition is :",Ret)

    Ret = Subtraction(No1,No2)
    print("Subtraction is :",Ret)

    Ret = Multiplication(No1,No2)
    print("Multiplication is :",Ret)

    Ret = Division(No1,No2)
    print("Division is :",Ret)


if __name__=="__main__":
    main()