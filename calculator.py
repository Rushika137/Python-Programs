print("----calculator----")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. division")

def calculate_values():
    a = int(input("enter the operator choice: "))
    while a<1 and a>4:
        print("invalid operator")
        a = int(input("enter the operator choice: "))

    b = float(input("enter first number: "))
    c = float(input("enter second number: "))

    if a == 1:
        print("result =", b + c)
    elif a == 2:
        print("result =", b - c)
    elif a == 3:
        print("result =", b * c)
    elif a == 4:
        if c == 0:
            print("can't divide by zero")
        else:
            print("result =", b / c)
   

while True:
    calculate_values()
    while True:
        k = input("do you want to continue again? (yes/no): ").lower()
        if k == "yes":
            break                         
        elif k == "no":
            print("thank you for using")
            exit()                         
        else:
            print("enter yes or no.")    
