#Write a program which accepts one number and displays the below pattern.

def pattern(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print("*",end="")
        print()
    
def main():
    No = int(input("Enter Number :"))
    pattern(No)

if __name__ == "__main__":
    main()