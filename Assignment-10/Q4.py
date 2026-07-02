#write a program which accepts one number and prints all even number till that number

def even(value):
    Arr = []
    for i in range(2,value+1,2):
        Arr.append(i)
    return Arr
    
def main():
    value = int(input("Enter Number :"))
    Ret = even(value)
    print("even numbers are : ")

    for no in Ret:
        print(no)

if __name__ == "__main__":
    main()