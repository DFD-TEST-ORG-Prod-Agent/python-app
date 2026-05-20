import os
import sys

def main():
    print("Python Sample App")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # File operations
    with open("output.txt", "w") as f:
        f.write(f"User: {name}\n")
    
    # Simple calculation
    result = calculate(10, 20)
    print(f"10 + 20 = {result}")

def calculate(a, b):
    return a + b

def read_config(path):
    # Potential security issue for scanning
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    main()
