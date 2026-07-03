#write a program which accepts one number and prints binary equivalent

def binary(No):
    return bin(No)

def main():
    value=int(input("Enter Number :"))
    Ret = binary(value)
    print(Ret)

if __name__=="__main__":
    main()
