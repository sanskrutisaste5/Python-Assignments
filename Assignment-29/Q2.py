#write a program which accepts a file name from the user , opens that file and displays the entire contents on the console
def main():

    try:
        filename = input("enter file name :")

        fobj = open(filename,"r")
        print("file opened")

        Data = fobj.read()
        print(Data)

        fobj.close()

    except FileNotFoundError as fobj:
        print(" file not found")

if __name__ == "__main__":
    main()