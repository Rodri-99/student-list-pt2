def list_names(students):
    for index, student in enumerate(students):
        print(f"{index + 1}. {student['name']}")

def get_new_student():
    new_student = {}
    new_student['name'] = input("Enter student's name: ")
    new_student['hometown'] = input("Enter student's hometown: ")
    new_student['favorite_food'] = input("Enter student's favorite food: ")
    return new_student

students = [
    { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
    { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
    { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]

while True:
    print("Type 'add' to create a new student")
    print("Type 'view' to look at existing students")
    print("Type 'quit' to exit the program")
    choice = input("Enter your choice: ")

    if choice == 'add':
        new_student = get_new_student()
        students.append(new_student)
        print("New student added successfully!")
    elif choice == 'view':
        list_names(students)
        selection = int(input("Enter the index of the student you want to view: ")) - 1
        if selection < 0 or selection >= len(students):
            print("Invalid index!")
        else:
            selected_student = students[selection]
            print(f"Name: {selected_student['name']}")
            option = input("Enter 'hometown' or 'favorite_food' to view that information: ")
            if option == 'hometown':
                print(f"Hometown: {selected_student['hometown']}")
            elif option == 'favorite_food':
                print(f"Favorite Food: {selected_student['favorite_food']}")
            else:
                print("Invalid option!")
    elif choice == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")