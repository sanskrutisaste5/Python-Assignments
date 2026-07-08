#Write a program which accepts one number from user and checks whether the number is prime or not.

def prime(No):
    if No < 2:
        return False
    
    for i in range(2,No):
        if No % i == 0 :
            return False
   
    return True
        
def main():
    No = int(input("Enter Number :"))
    Ret = prime(No)

    if (Ret == True):
        print("It is prime number ")
    else :
        print("It is not prime number")

if __name__ == "__main__":
    main()