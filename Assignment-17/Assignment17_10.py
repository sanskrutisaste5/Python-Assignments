#

def addition(No):
    sum = 0
    
    while No > 0:
        Digit = No % 10
        sum = sum + Digit
        No = No //10
    return sum

def main():
    No = int(input("Enter Number :"))
    Ret = addition(No)
    print(Ret)

if __name__ == "__main__":
    main()