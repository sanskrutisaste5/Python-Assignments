#write a program which accepts one number and prints sum of digits

def sum(No):
    sum = 0
    while(No>0):
        Digit = No % 10
        sum = sum + Digit
        No = No // 10
    return sum

def main():
    value = int(input("Enter number :"))
    Ret = sum(value)
    print(Ret)

if __name__ =="__main__":
    main()