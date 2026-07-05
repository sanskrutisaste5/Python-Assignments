# write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce

Product = lambda No1,No2 : No1*No2

def main():
    Values = [1,2,3,4]

    Data = reduce(Product,Values)
    print("Product is :",Data)

if __name__ == "__main__":
    main()