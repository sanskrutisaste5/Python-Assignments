#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

from functools import reduce
def prime (No):
    if No<2:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

Multiply = lambda No :No*2

Maximum = lambda No1,No2 : No1 if No1>No2 else No2 

def main():
    
    List = [2,70,11,10,17,23,31,77]
    print("input list is :",List)

    Data = list(filter(prime,List))
    print("List after filter:", Data)

    Data1 = list(map(Multiply, Data))
    print("List after map:", Data1)

    Data2 = reduce(Maximum, Data1)
    print("Output of reduce:", Data2)

if __name__ == "__main__":
    main()