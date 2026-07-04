#write a lambda function which accepts one number and returns square of that number
Square = lambda No1 : No1*No1

def main():
    Value = int(input("Enter the number :"))
    Ret = Square(Value)
    print("Square is :",Ret)

if __name__ == "__main__":
    main()