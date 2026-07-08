#Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all elements from that list.
def Add(Arr):
    sum = 0

    for no in Arr:
        sum = sum + no

    return sum


def main():
    Arr = []
    size = int(input("enter number :"))
    for i in range(size):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = Add(Arr)
    print(Ret)
    
if __name__ == "__main__":
    main()
