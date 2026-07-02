#2.Write a program which contains one function ChkGreater() that accepts 
# two numbers and prints the greater number.

def ChkGreater(No1,No2):
    
    if(No1>No2):
        return No1
    else:
        return No2

def main():

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret = ChkGreater(No1,No2)
    print("Greater number is :",Ret)

if __name__ =="__main__":
    main()



   


