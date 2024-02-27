def register_user():
    # Prompt the user for their information
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")

    # Format the user's information
    user_info = f"{username}\n{password}\n{phone_number}\n{email}\n\n"

    filename = "user_registrations.txt"

    # Append the information to the text file, create if not exists
    with open(filename, 'a') as file:
        file.write(user_info)

    print(f"User registered successfully. Information appended in {filename}")

if __name__ == "__main__":
    register_user()
