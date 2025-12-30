# Student Management System
# Author: Sanjay

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    students[roll] = {"Name": name, "Marks": marks}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['Name']}, Marks: {info['Marks']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(students[roll], "\n")
    else:
        print("Student not found.\n")

while True:
    print("1.Add  2.View  3.Search  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")
