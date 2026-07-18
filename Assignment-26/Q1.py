class Demo:
    #class variable
    value = 100

    def __init__(self,No1,No2):
        self.no1 = No1
        self.no2 = No2

    def Fun(self):
        print("fun method")
        print("No1 =", self.no1)
        print("No2=", self.no2)

    def Gun(self):
        print("gun method")
        print("No1 =", self.no1)
        print("No2=", self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()