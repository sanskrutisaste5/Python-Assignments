#Accept one file name and one string from the user and return the frequency of that string from the file.
import sys

def main():
    try:

        file = open(sys.argv[1],"r")
        Data = file.read()

        string = input("enter string to search:")
        Count = Data.count(string)    #count frequency

        print("frequency of",string, "is",Count)

        file.close()

    except Exception as eobj:
        print(eobj)

if __name__ =="__main__":
    main()