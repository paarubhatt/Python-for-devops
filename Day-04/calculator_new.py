import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2  

def multiplication(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator_new.py <num1> <num2> <operation>")
        print("Example: python calculator_new.py 55 45 add")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    operation = sys.argv[3].lower()

    if operation == "add":
        print("Result:", addition(num1, num2))
    elif operation == "sub":
        print("Result:", subtraction(num1, num2))
    elif operation == "mul":
        print("Result:", multiplication(num1, num2))
    else:
        print("Unsupported operation. Use 'add', 'sub', or 'mul'.")
