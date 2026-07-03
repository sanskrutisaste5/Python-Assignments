#write a program which accepts one character and checks whether it is vowel or constant

def check(char):
    if ((char == "a")or(char == "e")or(char == "i")or(char == "o")or(char == "u")):
        return True
    else:
        return False

def main():
    value = input("Enter the Character :")
    Ret = check(value)

    if (Ret == True):
        print("Vowel")
    else:
        print("consonant")
    
if __name__ == "__main__":
    main()