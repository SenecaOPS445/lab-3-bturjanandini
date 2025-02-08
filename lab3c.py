#!/usr/bin/env python3

# Author ID: [bturjanandinidia]

def operate(number1, number2, operator):
    # Function to operate based on the operator
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Test the operate function
    print(operate(10, 5, 'add'))          # Should print 15
    print(operate(10, 5, 'subtract'))     # Should print 5
    print(operate(10, 5, 'multiply'))     # Should print 50
    print(operate(10, 5, 'divide'))       # Should print error message

