#write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number 

Square = lambda No :No*No

def main():
    No = [1,2,3,4]

    Data= list(map(Square,No))
    print("list of square is :",Data)

if __name__ == "__main__":
    main()