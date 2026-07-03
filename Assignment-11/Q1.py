#write a program which accepts one number and checks whether it is prime or not

def prime(No):
    count = 0
    for i in range(1,No+1):
        if (No % i == 0):
            count = count + 1
    if (count==2):
        return True
    else:
        return False
    
def main():
    No = int(input("Enter Number :"))
    Ret = prime(No)

    if(Ret == True):
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()