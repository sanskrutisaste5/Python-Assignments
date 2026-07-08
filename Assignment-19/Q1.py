#Write a program which contains one lambda function which accepts one parameter and returns power of two.

Power = lambda No : 2**No

def main():
    No = int(input("Enter Number :"))
    Ret = Power(No)
    print("power is :",Ret)
   
if __name__ == "__main__":
    main()