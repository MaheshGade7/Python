def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return number == sum(d ** power for d in digits)

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_number(number, check_type):
    switch_case = {
        "armstrong": is_armstrong_number,
        "palindrome": is_palindrome_number,
        "prime": is_prime_number,
    }

    if check_type in switch_case:
        return switch_case[check_type](number)
    else:
        raise ValueError("Invalid check type. Choose from 'armstrong', 'palindrome', or 'prime'.")

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        check_type = input("Enter the type of check (armstrong, palindrome, prime): ").strip().lower()
        result = check_number(number, check_type)
        print(f"Is {number} a {check_type} number? {result}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
