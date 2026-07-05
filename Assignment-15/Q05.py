#write a lambda function using reduce() which accepts a list of numbers and returns the max element

from functools import reduce

Max = lambda No1,No2 : No1 if No1>No2 else No2

def main():
    Values = [1,2,3,4,5,6]

    Data = reduce(Max,Values)
    print("Maximum number is :",Data)

if __name__ == "__main__":
    main()