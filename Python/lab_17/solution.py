students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks in Subject {i+1}: "))
        marks.append(mark)

    students[roll_no] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- All Student Records ---")

    for roll_no, details in students.items():
        total = sum(details["marks"])
        percentage = total / len(details["marks"])

        print("\nRoll No:", roll_no)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])
        print("Marks:", details["marks"])
        print("Percentage:", percentage)


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("Student Found!")
        print(students[roll_no])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no in students:
        students[roll_no]["name"] = input("Enter New Name: ")
        students[roll_no]["age"] = int(input("Enter New Age: "))
        students[roll_no]["course"] = input("Enter New Course: ")

        print("Student record updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")