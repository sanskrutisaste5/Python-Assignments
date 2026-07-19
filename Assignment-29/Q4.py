#write a program which accepts two file names through command linearguments and compare the contents of both files 
import sys

def main():
    print(sys.argv)
    try:

        file1 = open(sys.argv[1], "r") # Opens in read mode.
        file2 = open(sys.argv[2], "r")

        Data1 = file1.read() #read the content
        Data2 = file2.read()

        if(Data1 == Data2):
            print("Success")

        else:
            print("Failure")

        file1.close()
        file2.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()