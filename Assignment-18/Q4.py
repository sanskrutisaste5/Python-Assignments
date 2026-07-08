#Write a program which accepts N numbers from the user and stores them into a List. Accept one another number from the user and return the frequency of that number from the list.

def Frequency(Arr, Value):
    Count = 0

    for No in Arr:
        if No == Value:
            Count = Count + 1

    return Count

def main():
    Arr = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Arr.append(No)

    Value = int(input("Enter number to search: "))

    Ret = Frequency(Arr, Value)
    print("Frequency is:", Ret)

if __name__ == "__main__":
    main()