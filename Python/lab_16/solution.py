def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b


def power(a, b):
    return a ** b


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def display_history(history):
    print("\n--- Calculation History ---")
    if not history:
        print("No history available.")
    else:
        for item in history:
            print(item)


def main():
    history = []

    while True:
        print("\n================================")
        print("       UTILITY CALCULATOR")
        print("================================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Temperature Conversion")
        print("8. View History")
        print("9. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice (1-9): "))

            if choice == 9:
                confirm = input("Are you sure you want to exit? (y/n): ")
                if confirm.lower() == 'y':
                    print("Thank you for using Utility Calculator!")
                    break
                else:
                    continue

            elif choice == 8:
                display_history(history)

            elif choice == 7:
                c = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(c)
                print("Temperature in Fahrenheit:", result)
                history.append(f"{c} Celsius = {result} Fahrenheit")

            elif choice in [1, 2, 3, 4, 5, 6]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    result = add(a, b)
                    operator = "+"

                elif choice == 2:
                    result = subtract(a, b)
                    operator = "-"

                elif choice == 3:
                    result = multiply(a, b)
                    operator = "*"

                elif choice == 4:
                    result = divide(a, b)
                    operator = "/"

                elif choice == 5:
                    result = modulus(a, b)
                    operator = "%"

                elif choice == 6:
                    result = power(a, b)
                    operator = "**"

                print("Result:", result)

                if not isinstance(result, str):
                    history.append(f"{a} {operator} {b} = {result}")

            else:
                print("Invalid choice! Please select between 1 and 9.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()