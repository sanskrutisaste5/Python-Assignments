#Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5, otherwise returns False.

def Divisible(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    Number = int(input("Enter Number :"))
    Ret = Divisible(Number)
    print(Ret)

if __name__ == "__main__":
    main()