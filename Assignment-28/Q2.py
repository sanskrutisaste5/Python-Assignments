#Count Words in a File

def main():
    try:

        file = input("enter file name: ")
        fobj = open(file, "r")      # Open the file

        Data = fobj.read()          # Read the file contents


        words = Data.split()    # splits data into words

        print("Total number of words are :",len(words))

        fobj.close()

    except Exception as eobj:
        print((eobj))

if __name__ == "__main__":
    main()