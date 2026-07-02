def Cube(No):
    Ans = No * No* No
    return Ans

def main():
    No = int(input("Enter the number :"))

    Ret = Cube(No)
    print("Cube is :",Ret)

if __name__ =="__main__":
    main()