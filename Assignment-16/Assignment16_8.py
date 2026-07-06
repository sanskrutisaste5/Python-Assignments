#Write a program which accepts a number from the user and prints that number of * (asterisks) on the screen.

def star(No):
    return No * "*"

def main():
    Number = int(input("Enter Number :"))
    Ret = star(Number)
    print(Ret)

if __name__ == "__main__":
    main()