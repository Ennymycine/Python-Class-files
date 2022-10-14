#simple calculator
#This function adds two numbers
def add(x, y, z):
    return x + y + z

# This function subtracts two numbers
def subtract(x, y, z):
    return x - y - z

# This function multiplies two numbers
def multiply(x, y, z):
    return x * y  * z

# This function divides two numbers
def divide(x, y, z):
    return x / y / z


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        if choice == '1':
            print(num1, "+", num2, num3, "=", add(num1, num2, num3))

        elif choice == '2':
            print(num1, "-", num2, num3, "=", subtract(num1, num2, num3))

        elif choice == '3':
            print(num1, "*", num2, num3, "=", multiply(num1, num2, num3))

        elif choice == '4':
            print(num1, "/", num2, num3, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
    



