#write a program which accepts one number and prints that many numbers starting form 1
def main():
    Value = int(input("Enter a number :"))

    for i in range(1,Value+1):
        print(i)

if __name__ == "__main__":
    main()