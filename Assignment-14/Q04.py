#write a lambda function which accepts two numbers and returns minimum number

minimum = lambda No1,No2: No1 if (No1<No2) else No2
    
def main():
    No1 = int(input("Enter No1 :"))
    No2 = int(input("Enter No2 :"))

    Ret = minimum(No1,No2)
    print("minimum value is :",Ret)

if __name__ == "__main__":
    main()