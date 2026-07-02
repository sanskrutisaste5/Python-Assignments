#write a program that accepts one number and prints square of that number

def Square(a):
    Ans = a*a 
    return Ans

def main():
    value = int(input("Enter a number :"))

    Ret = Square(value)
    print("Square is :",Ret)

if __name__ =="__main__":
    main()
