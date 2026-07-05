#write a lambda function using reduce()which accepts a list of numbers and returns addition of all elements

from functools import reduce

Addition = lambda No1,No2: No1 + No2

def main():
    Values = [1,2,3,4,5,6,7,8,9]

    Data = reduce(Addition,Values)
    print("Addition is :",Data)

if __name__ == "__main__":
    main()
