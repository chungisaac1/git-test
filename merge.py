# merge.py

def greet():
    print("Hello from the junseon branch") 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    print("This is the main function")
    greet()
    result_add = add(10, 5)
    result_sub = subtract(10, 5)
    result_mul = multiply(10, 5)
    result_div = divide(10, 5)
    print(f"Add: {result_add}, Subtract: {result_sub}, Multiply: {result_mul}")

if __name__ == "__main__":
    main()