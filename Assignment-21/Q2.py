#Design a Python application that creates two threads.

#Thread1 should calculate and display the maximum element from a list.
#Thread2 should calculate and display the minimum element from the same list.
#The list should be accepted from the user.

import threading

def Maximum(Arr):
    Max = Arr[0]

    for No in Arr:
        if No > Max:
            Max = No

    print("Maximum element:", Max)


def Minimum(Arr):
    Min = Arr[0]

    for No in Arr:
        if No < Min:
            Min = No

    print("Minimum element:", Min)


def main():
    Arr = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Arr.append(No)

    tobj1 = threading.Thread(target=Maximum, args=(Arr,))
    tobj2 = threading.Thread(target=Minimum, args=(Arr,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

if __name__ == "__main__":
    main()