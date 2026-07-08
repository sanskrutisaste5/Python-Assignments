#Design a Python application that creates three threads named Small, Capital, and Digits.
#All threads should accept a string as input.
#The Small thread should count and display the number of lowercase characters.
#The Capital thread should count and display the number of uppercase characters.
#The Digits thread should count and display the number of numeric digits.
#Each thread must also display:

#Thread ID
#Thread Name

import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if ch >= 'a' and ch <= 'z':
            Count = Count + 1

    print("Small characters:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def Capital(Str):
    Count = 0

    for ch in Str:
        if ch >= 'A' and ch <= 'Z':
            Count = Count + 1

    print("Capital characters:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def Digits(Str):
    Count = 0

    for ch in Str:
        if ch >= '0' and ch <= '9':
            Count = Count + 1

    print("Digits:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)


def main():
    Str = input("Enter String: ")

    tobj1 = threading.Thread(target=Small, args=(Str,), name="Small")
    tobj2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    tobj3 = threading.Thread(target=Digits, args=(Str,), name="Digits")

    tobj1.start()
    tobj2.start()
    tobj3.start()

    tobj1.join()
    tobj2.join()
    tobj3.join()


if __name__ == "__main__":
    main()