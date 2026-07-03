#write a program which accepts radius of circle and prints area of circle

def circle(PI,Radius):
    Area = PI*Radius*Radius
    return Area

def main():
    PI=3.14
    Radius = int(input("Enter the Radius :"))

    Ret = circle(PI,Radius)
    print("Area of circle is : ",Ret)


if __name__ =="__main__":
    main()