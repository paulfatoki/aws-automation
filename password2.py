correct_password = "password123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Success! You've entered the correct password.")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Maximum attempts exceeded. You are now locked out.")