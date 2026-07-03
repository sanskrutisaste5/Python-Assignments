#write a program which accepts length and breadth of rectangle and prints area

def rectangle(Length,Breadth):
    Area = Length*Breadth
    return Area

def main():
    Length=int(input("Enter the Length :"))
    Breadth=int(input("Enter the Breadth :"))
    
    Ret = rectangle(Length,Breadth)
    print("Area of rectangle is :",Ret)


if __name__ == "__main__":
    main()