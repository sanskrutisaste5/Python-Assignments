#write a program which accepts one number and prints all odd numbers till that number
def odd(value):
    Arr = list()

    for i in range(1,value+1,2):
        Arr.append(i)
    return Arr

def main():
    value = int(input("Enter Number :"))
    Ret = odd(value)
    print("Odd numbers are :")
    
    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()
