#write a lambda function using reduce() which accepts a list of numbers and returns the min element

from functools import reduce

Min = lambda No1,No2: No1 if No1<No2 else No2

def main():
    Values = [1,2,3,4,5,6,7,8,9]

    Data = reduce(Min,Values)
    print("Minimum element is :",Data)

if __name__ =="__main__":
    main()


