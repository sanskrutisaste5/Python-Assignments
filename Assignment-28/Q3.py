#Display File Contents Line by Line
def main():
    try:

        file = input("Enter file name: ")

        fobj = open(file, "r")      # Open the file

        for line in fobj:
            print(line, end="")     # Display one line at a time

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()