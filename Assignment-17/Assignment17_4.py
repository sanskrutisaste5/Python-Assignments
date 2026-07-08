#Write a program which accepts one number from user and returns the addition of its factors.

def Addition(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
    return sum

def main():
    No = int(input("Enter Number :"))

    Ret = Addition(No)
    print("addition of factors :",Ret)

if __name__ == "__main__":
    main()