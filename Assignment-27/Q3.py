class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime Number
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    # Check Perfect Number
    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        if Sum == self.Value:
            return True
        else:
            return False

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i

        return Sum


# Create Objects
Obj1 = Numbers(int(input("Enter First Number: ")))
Obj2 = Numbers(int(input("Enter Second Number: ")))

# First Object
print("\nFor First Number:")
print("Prime:", Obj1.ChkPrime())
print("Perfect:", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())

# Second Object
print("\nFor Second Number:")
print("Prime:", Obj2.ChkPrime())
print("Perfect:", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors:", Obj2.SumFactors())