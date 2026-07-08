#Write a program which accepts N numbers from the user and stores them into a List. Return the maximum number from that list.

def Max(Arr):
    Max = Arr[0]

    for no in Arr:
        if no > Max:
            Max = no

    return Max


def main():
    Arr = []
    size = int(input("enter number :"))
    for i in range(size):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = Max(Arr)
    print(Ret)
    
if __name__ == "__main__":
    main()