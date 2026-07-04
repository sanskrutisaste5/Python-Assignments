#write a lambda function which accepts one number and returns True if number is odd otherwise False

Odd = lambda No : False if (No % 2 == 0) else True

def main():
    value= int(input("Enter Number :"))
    Ret = Odd(value)
    print(Ret)

if __name__ == "__main__":
    main()
