#
def check(value):
    if((value % 3 == 0) and (value % 5 == 0)):
        return True

    else:
        return False

def main():
    
    print("Enter the Number :")
    value = int(input())

    Ret = check(value)
    if (Ret == True):
        print("Number is divisible by 3 and 5 ")

    else:
        print("Number is not divisible by 3 and 5 ")

if __name__ == "__main__":
    main()