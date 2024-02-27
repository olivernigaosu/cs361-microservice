Registration Microservice Overview
This document provides instructions for interacting with the Registration Microservice, designed to register users by storing their information in a text file and allowing for the retrieval of this data.

Requesting Data
To add user information to the microservice, you need to provide the username, password, phone number, and email. This is done through running the register_user.py script.

Example Call: python register_user.py

After executing the script, you will be prompted to enter the user's details:

Enter your username: johndoe
Enter your password: password123
Enter your phone number: 123-456-7890
Enter your email: johndoe@example.com

The information will then be saved to a file named user_registrations.txt in the current directory. If the file already exists, the new user's information will be appended to it.

Receiving Data
To retrieve and process the user data stored by the microservice, run the read_registrations.py script. This script reads the user_registrations.txt file, processes the user information, and outputs it.

Example Call: python read_registrations.py

This command will print the details of all registered users to the console, formatted as follows:

User Details:
Username: johndoe
Password: password123
Phone Number: 123-456-7890
Email: johndoe@example.com


![cs361 UML (1)](https://github.com/olivernigaosu/cs361-microservice/assets/156348566/412a0fe5-058e-485b-8126-291ebbce9e2c)
