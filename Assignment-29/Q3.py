#write a program which accepts an existing file name through command line arguments , creates a new file name demo.txt and copied all contents from the given file into demo.txt
import sys        #to access command line

def main():
    try:

        file = open(sys.argv[1], "r") #read 
        Data = file.read()

        file1 = open("Demo.txt","w")   # w = create and open
        file1.write(Data)

        file.close()
        file1.close()

    except Exception as eobj:
        print("file not found")

if __name__ == "__main__":
    main()