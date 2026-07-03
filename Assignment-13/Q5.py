#write a program whic accepts marks and display grade

def grade(Marks):
    if (Marks>= 75):
        return "Distinction"
    elif(Marks>=60):
        return "First Class"
    elif(Marks>=50):
        return "Second Class"
    else:
        return "Fail"

def main():
    Marks= int(input("Enter Marks :"))
    Ret = grade(Marks)
    print(Ret)

if __name__ =="__main__":
    main()