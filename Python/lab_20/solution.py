# Lab 20 - Daily Log Book

filename = "daily_log.txt"


# Function to append log entry
def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")

    print("[SUCCESS] New entry logged to", filename)


# Function to display complete log
def display_log(filename):
    with open(filename, "r") as file:
        entries = file.readlines()

    print("\n========== DAILY LOG BOOK ==========")

    if entries:
        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry.strip()}")

        print("\nTotal logged entries:", len(entries))
    else:
        print("No log entries found.")


# Create file with sample entries if it does not exist
try:
    with open(filename, "x") as file:
        file.write("System startup verified.\n")
        file.write("Morning office setup completed.\n")
        file.write("Network security check passed.\n")
except FileExistsError:
    pass


# Main program
while True:
    print("\n================================")
    print("       OFFICE DAILY LOG BOOK")
    print("================================")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")