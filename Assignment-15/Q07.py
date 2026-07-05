#write a lambda function using filter() which accepts a list of string and returns a list of strings having length greater than 5 

string = lambda Value : len(Value)>5

def main():
    Ret = ["pune","mumbai","indore","nashik","nagpur"]

    Data = list(filter(string,Ret))
    print("strings having length greater than 5",Data)
if __name__ == "__main__":
    main()