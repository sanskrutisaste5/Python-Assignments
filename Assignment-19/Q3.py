#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
from functools import reduce

Numbers= lambda No : No >=70 and No<=90

Increment = lambda No : No+10

product = lambda No1,No2 : No1*No2


def main():
    Arr = [4,34,36,76, 68, 24, 89, 23, 86, 90, 45, 70]
    print("Input list is : ",Arr)

    Data = list(filter(Numbers,Arr))
    print (Data)

    Data1 = list(map(Increment,Data))
    print(Data1)

    Data2 = reduce(product,Data1)
    print (Data2)
    
if __name__ == "__main__":
    main()