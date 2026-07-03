#write a program which accepts one number and prints sum of digits

def rev(No):
    rev = 0
    while(No>0):
        Digit = No % 10
        rev = (rev*10)+Digit
        No = No // 10
    return rev

def main():
    value = int(input("Enter number :"))
    Ret = rev(value)
    print(Ret)

if __name__ =="__main__":
    main()