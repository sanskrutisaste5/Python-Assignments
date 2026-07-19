# Copy File Contents into Another File

def main():
    try:
        file1 = input("Enter existing file name: ")
        file2 = input("Enter new file name: ")

        fobj1 = open(file1, "r")      # Open existing file
        Data = fobj1.read()           # Read contents

        fobj2 = open(file2, "w")      # Create/Open new file
        fobj2.write(Data)             # Write contents

        fobj1.close()
        fobj2.close()

        print("Contents copied successfully.")

    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()