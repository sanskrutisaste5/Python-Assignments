#write a lambda function which accepts two numbers and returns Addition

Addition = lambda No1,No2: No1 + No2

def main():
    No1 = int(input("Enter No1 :"))
    No2 = int(input("Enter No2 :"))
    Ret = Addition(No1,No2)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()