def read_and_process_registrations(filename="user_registrations.txt"):
    # Check if the file exists
    try:
        with open(filename, 'r') as file:
            # Read the entire file and split into entries by double newlines
            content = file.read().strip()
            users = content.split("\n\n")  # Splitting by double newline to get each user's info as one chunk

            for user in users:
                # Each user's info is separated by a single newline
                details = user.split("\n")
                print("User Details:")
                print(f"Username: {details[0]}")
                print(f"Password: {details[1]}")
                print(f"Phone Number: {details[2]}")
                print(f"Email: {details[3]}\n")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

if __name__ == "__main__":
    read_and_process_registrations()
