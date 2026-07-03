#write a program which accepts one number and prints that many numbers in reverse order

def main():
    value = int(input("Enter the Number :"))

    for i in range(value,0,-1):
        print(i)

if __name__ =="__main__":
    main()