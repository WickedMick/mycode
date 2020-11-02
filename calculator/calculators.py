#   Easy calculator
#!/usr/bin/env python3
#  Addition
def add(x,y):
    return x + y
    
#  Subtract
def subtract(x, y):
    return x - y

#  Multiply
def multiply(x, y):
    return x * y

#  Divide
def divide(x, y):
    return x / y

#  Operation selection
print("Please select")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

        #Take input
select = int(input("Select operation 1, 2, 3, 4:"))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

#Here is the operation in an if loop
if select == 1:
    print(x, "+", y, "=",
        add(x, y))
elif select == 2:
    print(x, "-", y, "=", # missing a comma
        subtract(x, y))
elif select == 3:
    print(x, "*", y, "=",
        multiply(x, y))
elif select == 4:
    print(x, "/", y, "=",
        divide(x, y))
else:
    print("1 through 4, please")

