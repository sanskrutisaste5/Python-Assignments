#write a program that accepts one number and prints its factors

def factor(No):
    Arr = list()

    for i in range(1,No+1):
        if(No % i == 0):
            Arr.append(i)
    return Arr  

def main():
    value= int(input("Enter Number :"))
    Ret = factor(value)

    for no in Ret:
        print(no)
    

if __name__ =="__main__":
    main()