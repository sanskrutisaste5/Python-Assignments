#Create one module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accept two parameters as number and perform the operation. Write one Python program which calls all the functions from Arithmetic module by accepting the parameters from user.

from Arithmetic import Add,Sub,Mult,Div

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter second Number :"))

    Ret = Add(No1,No2)
    print(Ret)

    Ret = Sub(No1,No2)
    print(Ret)

    Ret = Mult(No1,No2)
    print(Ret)

    Ret = Div(No1,No2)
    print(Ret)

if __name__ == "__main__":
    main()