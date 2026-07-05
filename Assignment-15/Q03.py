#write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers

def Odd(No):
    return No % 2 != 0 

def main():
    values=[1,2,3,4,5,6,7,8,9]

    Data = list(filter(Odd,values))
    print("List of odd numbers is :",Data)

if __name__ == "__main__":
    main() 
