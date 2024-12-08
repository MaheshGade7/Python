import sqlite3
import re


# Function to connect to database
def create_connection():
    """Create and return a database connection."""
    try:
        # Connect to SQLite database (or create one if it doesn't exist)
        conn = sqlite3.connect("user_data.db")
        print("Database connection established.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


# Function to initialize database table
def initialize_db(conn):
    """Create the users table if it doesn't already exist."""
    try:
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
        """
        conn.execute(query)
        conn.commit()
        print("Database initialized with table `users`.")
    except Exception as e:
        print(f"Error initializing database: {e}")


# Function to validate email format
def validate_email(email):
    """Check if email is in a valid format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    return False


# Function to validate age
def validate_age(age):
    """Check if age is a valid number and meets conditions."""
    try:
        age = int(age)
        if age >= 0:
            return True
        return False
    except ValueError:
        return False


# Function to insert a user into the database
def insert_user(conn, username, email, age):
    """Insert a new user into the database after validation."""
    if not username.strip():
        print("Validation Error: Username cannot be empty.")
        return
    if not validate_email(email):
        print("Validation Error: Invalid email address.")
        return
    if not validate_age(age):
        print("Validation Error: Invalid age.")
        return

    try:
        query = "INSERT INTO users (username, email, age) VALUES (?, ?, ?)"
        conn.execute(query, (username, email, int(age)))
        conn.commit()
        print("User inserted successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username or email already exists.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Function to read users from the database
def fetch_users(conn):
    """Fetch and display all users from the database."""
    try:
        query = "SELECT * FROM users"
        cursor = conn.execute(query)
        users = cursor.fetchall()
        if users:
            print("Current Users in Database:")
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Age: {user[3]}")
        else:
            print("No users found in the database.")
    except Exception as e:
        print(f"Error fetching data: {e}")


# Main function for interaction
def main():
    # Establish database connection
    conn = create_connection()
    if not conn:
        return

    # Initialize the database table
    initialize_db(conn)

    # Menu loop
    while True:
        print("\nSelect an option:")
        print("1. Insert User")
        print("2. Fetch Users")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Insert user flow
            username = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            age = input("Enter age: ").strip()
            insert_user(conn, username, email, age)

        elif choice == "2":
            # Fetch and display all users
            fetch_users(conn)

        elif choice == "3":
            # Exit the application
            print("Exiting...")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
