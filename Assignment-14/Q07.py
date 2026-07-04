#write a lambda function which accepts one number ad returns True if divisible by 5

Divisible = lambda No: True if (No % 5 == 0) else False

def main():
    Value = int(input("Enter Number :"))
    Ret = Divisible(Value)
    print(Ret)

if __name__ == "__main__":
    main()