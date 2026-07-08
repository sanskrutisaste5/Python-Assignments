#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce

even= lambda No : No % 2 == 0

square = lambda No: No * No

Addition = lambda No1,No2 :No1 + No2 

def main():
    Arr = []

    List = [5,2,3,4,3,4,1,2,8,10]
    print("input list is :",List)

    Data = list(filter(even,List))
    print(Data)

    Data1 = list(map(square,Data))
    print(Data1)

    Data2 = reduce(Addition,Data1)
    print(Data2)

if __name__ == "__main__":
    main()