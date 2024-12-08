import re

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha() and len(name) > 1:
            return name
        print("Invalid name. Please enter alphabetic characters only and ensure it is at least 2 characters long.")

def get_valid_email():
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input("Enter your email: ").strip()
        if re.match(email_regex, email):
            return email
        print("Invalid email. Please enter a valid email address (e.g., user@example.com).")

def get_valid_phone_number():
    phone_regex = r'^\+?[0-9]{10,15}$'
    while True:
        phone = input("Enter your phone number (10-15 digits, optional '+'): ").strip()
        if re.match(phone_regex, phone):
            return phone
        print("Invalid phone number. Please enter a valid phone number with 10 to 15 digits.")

def main():
    print("Customer Details Input")
    name = get_valid_name()
    email = get_valid_email()
    phone_number = get_valid_phone_number()
    
    print("\nCustomer Details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")

if __name__ == "__main__":
    main()
