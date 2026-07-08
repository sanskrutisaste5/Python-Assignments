#Design a Python application that creates two separate threads named Even and Odd.

#The Even thread should display the first 10 even numbers.
#The Odd thread should display the first 10 odd numbers.
#Both threads should execute independently using the threading module.
#Ensure proper thread creation and execution.

import threading

def even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():

    tobj1 = threading.Thread (target=even )
    tobj2 = threading.Thread (target=odd )
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

if __name__ =="__main__":
    main()