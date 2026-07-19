#Count Lines in a File

def main():
    try:
        file = input("enter file name:")
        fobj = open(file,"r")

        count = 0

        for line in fobj:
            count = count + 1

        print("total number of lines :",count)

        fobj.close()

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()