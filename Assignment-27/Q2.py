class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print("Account holder name : ",self.Name )
        print("Current Balance : ",self.Amount )

    def Deposit(self):
        deposit = float(input("Enter amount to deposit: "))
        self.Amount += deposit
        print("Amount Deposited Successfully.")

    def Withdraw(self):
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance!")

    
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
# Create first object
Obj1 = BankAccount("Sanskruti", 50000)

Obj1.Display()
Obj1.Deposit()
Obj1.Display()
Obj1.Withdraw()
Obj1.Display()
print("Interest =", Obj1.CalculateInterest())

# Create second object
Obj2 = BankAccount("Rahul", 30000)

Obj2.Display()
Obj2.Deposit()
Obj2.Display()
Obj2.Withdraw()
Obj2.Display()
print("Interest =", Obj2.CalculateInterest())
        