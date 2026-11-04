# Lab 18 - Mathematics Learning Tool

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function to generate Fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Main program
while True:
    print("\n================================")
    print("    MATHEMATICS LEARNING TOOL")
    print("================================")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == '1':
        num = int(input("Enter a non-negative integer: "))

        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Factorial of", num, "is:", factorial(num))

    elif choice == '2':
        terms = int(input("Enter number of terms: "))

        if terms <= 0:
            print("Please enter a positive number.")
        else:
            series = []

            for i in range(terms):
                series.append(fibonacci(i))

            print("Fibonacci Series:", series)

    elif choice == '3':
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")