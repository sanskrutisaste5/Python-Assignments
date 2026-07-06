#Write a program which contains one function named as ChkNum() which accepts one parameter as number. If the number is even then it should display "Even Number" otherwise display "Odd Number" on console.

def ChkNum(No):
    if (No % 2 == 0):
        return True
    else:
        return False

def main():
    number = int(input("Enter Number :"))
    Ret = ChkNum(number)

    if (Ret == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()