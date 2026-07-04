#write a lambda function which accepts one number and returns True if number is even otherwise False

EvenCheck = lambda No: True if (No % 2 == 0) else False
        

def main():
    Value = int(input("Enter Number :"))
    Ret = EvenCheck(Value)
    print(Ret)

if __name__ == "__main__":
    main()