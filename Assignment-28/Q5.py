# Search a Word in a File

def main():
    try:
        file = input("Enter file name: ")

        fobj = open(file, "r")

        Data = fobj.read()

        word = input("Enter word to search: ")

        if word in Data:
            print("Word found in the file.")
        else:
            print("Word not found in the file.")

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()