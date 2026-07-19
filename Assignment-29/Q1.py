#write a program which accepts a file name from the user and checks whether that file exists in the current directory or not
import os

def main():
    Ret = os.path.exists("Demo.txt")

    if(Ret == True):
        print("Demo.txt file exist")

    else:
        print("Demo.txt file does not exist")

if __name__ == "__main__":
        main()