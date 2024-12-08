def save_student_details():
    # Open the file in append mode to preserve existing data
    with open("student.txt", "a") as file:
        while True:
            print("Enter student details:")

            # Collecting student details from the user
            name = input("Name: ")
            roll_no = input("Roll Number: ")
            grade = input("Grade: ")
            age = input("Age: ")

            # Writing the student details to the file
            file.write(f"Name: {name}, Roll Number: {roll_no}, Grade: {grade}, Age: {age}\n")

            # Ask if the user wants to enter details of another student
            another = input("Do you want to add another student? (yes/no): ").strip().lower()
            if another != "yes":
                break

if __name__ == "__main__":
    save_student_details()
    print("Student details have been saved to 'student.txt'.")
