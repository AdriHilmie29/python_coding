#Write a program to make a simple calculator. The program should perform four basic operations (1-addition, 2-subtraction, 3-multiplication, and 4-division) 
#depending on the user’s choice. 
#The program will take two values from the user and the type of operation. The result will be displayed based on the operation chosen by the user. 
#The program will be repeated until user requests to stop.




def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

print(' ')

while True:
    operation = input("Choose operation(1/2/3/4): ")

    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("You entered the invalid input")
