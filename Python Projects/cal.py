def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

def calculator():
    operation = input('Enter operation (+, -, *, /): ')
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if operation == '+':
        print(num1, '+', num2, '=', add(num1, num2))
    elif operation == '-':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif operation == '*':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif operation == '/':
        print(num1, '/', num2, '=', divide(num1, num2))
    else:
        print('Invalid operation')

calculator()

