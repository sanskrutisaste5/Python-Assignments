#write a lambda function which accepts one number and returns cube of that number
Cube = lambda No1 : No1*No1*No1

def main():
    Value=int(input("Enter value :"))
    Ret = Cube(Value)
    print("Cube is :",Ret)

if __name__ == "__main__":
    main()