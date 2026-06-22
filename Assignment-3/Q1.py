def multiplication(No1,No2):
    return No1*No2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    Ret = multiplication(No1,No2)
    print("Multiplication is :",Ret)

if __name__ == "__main__":
    main()