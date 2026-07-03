#write a program which accepts one number and checks whether it is perfect number or not

def check(No):
    sum = 0
    for i in range (1,No):
        if(No % i==0):
            sum = sum + i

    if (sum == No):
            return True
    else:
            return False 

def main():
    No = int(input("Enter the Number :"))
    Ret = check(No)

    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not perfect Number")

if __name__ =="__main__":
    main()