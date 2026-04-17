# calculator_system.py
# Menu-Driven Calculator with Advanced Options

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def power(x, y): return x ** y
def modulus(x, y): return x % y

def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Modulus (x % y)")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "7":
            print("👋 Exiting Calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", power(num1, num2))
        elif choice == "6":
            print("Result:", modulus(num1, num2))
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    calculator()
