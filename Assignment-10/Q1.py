#write a program which accepts one number and prints multiplication table of that number

def table(value):
    Arr=[]

    for i in range(1,11):
        Arr.append(value*i) 

    return Arr

def main():
    print("Enter the number :")
    value = int(input())

    Ret=table(value)
    print("Multiplication table is :")
    for no in Ret:
        print(no)


if __name__=="__main__":
    main()

