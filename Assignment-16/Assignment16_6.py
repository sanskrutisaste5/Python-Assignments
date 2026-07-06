#Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

def check(No):
    if No > 0:
        return ("Positive")
    elif No < 0:
        return ("Negative")
    else:
        return ("zero")

def main():
    number = int(input("Enter Number :"))
    Ret = check(number)
    print (Ret)

if __name__ =="__main__":
    main()