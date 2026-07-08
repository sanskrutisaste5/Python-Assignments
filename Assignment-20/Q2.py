#Design a Python application that creates two threads named EvenFactor and OddFactor.

#Both threads should accept one integer number as a parameter.
#The EvenFactor thread should:
#Identify all even factors of the given number.
#Calculate and display the sum of even factors.
#The OddFactor thread should:
#Identify all odd factors of the given number.
#Calculate and display the sum of odd factors.
#After both threads complete execution, the main thread should display the message:
#"Exit from main"

import threading

def evenfactor(No):
    Sum = 0

    print("Even Factors are:")
    for i in range(1, No + 1):
        if (No % i == 0) and (i % 2 == 0):
            print(i)
            Sum = Sum + i
    print("Sum of Even Factors:", Sum)

def oddfactor(No):
    Sum = 0

    print("Odd Factors are:")
    for i in range(1, No + 1):
        if (No % i == 0) and (i % 2 != 0):
            print(i)
            Sum = Sum + i

    print("Sum of Odd Factors:", Sum)

def main():
    No = int(input("Enter Number: "))
    tobj1 = threading.Thread (target=evenfactor, args=(No,) )
    tobj2 = threading.Thread (target=oddfactor,args=(No,) )
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")

if __name__ =="__main__":
    main()