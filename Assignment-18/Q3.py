#Write a program which accepts N numbers from the user and stores them into a List. Return the minimum number from that list.

def Min(Arr):
    Min = Arr[0]

    for no in Arr:
        if no < Min:
            Min = no
    return Min


def main():
    Arr = []
    size = int(input("enter number :"))
    for i in range(size):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = Min(Arr)
    print(Ret)
    
if __name__ == "__main__":
    main()