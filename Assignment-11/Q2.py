#write a program which accepts one number and prints count of digits in that number

def count(No):
    count = 0
    while(No>0):
        count = count + 1
        No = No // 10
    return count

def main():
    
    value = int(input("enter number :"))
    Ret = count(value)
    print(Ret)

if __name__ == "__main__":
    main()