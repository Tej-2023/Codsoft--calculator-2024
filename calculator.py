def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

calculator()
