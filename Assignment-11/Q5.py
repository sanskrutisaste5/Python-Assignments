#write a program which accepts one number and checks whether it is pallindrom or not

def pallindrom(No):
    Temp = No
    rev = 0

    while(No>0):
        Digit = No % 10
        rev = (rev*10)+Digit
        No = No // 10

    if (Temp == rev):
        return True
    else:
        return False

def main():
    value = int(input("Enter number :"))
    Ret = pallindrom(value)
    
    if (Ret == True):
        print("Pallindrom")
    else:
        print("Not Pallindrom")

if __name__ =="__main__":
    main()