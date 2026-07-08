#Write a program which creates two threads as named small and capital. The small thread displays all lowercase characters and the capital thread displays all uppercase characters.

import threading

def small():
    print("Lowercase letters:")
    for ch in range(ord('a'), ord('z') + 1):
        print(chr(ch), end=" ")
    print()

def capital():
    print("Uppercase letters:")
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr(ch), end=" ")
    print()

def main():

    tobj1 = threading.Thread(target=small)
    tobj2 = threading.Thread(target=capital)

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()