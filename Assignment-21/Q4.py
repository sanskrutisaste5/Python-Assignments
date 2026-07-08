#Design a Python application that creates two threads.

#Thread1 should compute the sum of elements from a list.
#Thread2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.

import threading

def Sum(Arr):
    Total = 0

    for No in Arr:
        Total = Total + No

    print("Sum:", Total)


def Product(Arr):
    Ans = 1

    for No in Arr:
        Ans = Ans * No

    print("Product:", Ans)


def main():
    Arr = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Arr.append(No)

    tobj1 = threading.Thread(target=Sum, args=(Arr,))
    tobj2 = threading.Thread(target=Product, args=(Arr,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

if __name__ == "__main__":
    main()