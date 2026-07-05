#write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

even = lambda No1 : No1 % 2 == 0

def main():
    Values = [1,2,3,4,5,6,7,8,9]

    Data = list(filter(even,Values))
    
    print("Even numbers are :",Data)
    print("Count of even numbers :", len(Data))

if __name__ == "__main__":
    main()