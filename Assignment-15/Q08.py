#write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5 

Divisible = lambda No : No % 3 ==0 and No % 5 == 0

def main():
    Values = [10,11,12,13,14,15,16,17,18,19,20]

    Data = list(filter(Divisible,Values))
    print(Data,"Divisible by 3 and 5")

if __name__ == "__main__":
    main()