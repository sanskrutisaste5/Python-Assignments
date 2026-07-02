#
def sum(value):
    sum = 0
    for i in range(1,value+1):
        sum = sum + i
    return(sum)

def main():
    value = int(input("enter first number :"))
    Ret = sum(value)
    print("Sum of N natural numbers are : ",Ret)

if __name__ == "__main__":
    main()
