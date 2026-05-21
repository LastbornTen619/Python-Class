# 1. We start with a dictionary to store our users. 
# The username will be the 'key', and the password will be the 'value'.
user_database = {}

print("--- Welcome to the User System ---")

# 2. We use a 'while True' loop so the program keeps running until we choose to exit.
while True:
    print("\nWhat would you like to do?")
    print("1. Register a new user")
    print("2. Log in")
    print("3. Display total number of users")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    # --- OPTION 1: REGISTER ---
    if choice == "1":
        new_username = input("Create a username: ")
        
        # Check if the username already exists in our dictionary
        if new_username in user_database:
            print("That username is already taken! Try another one.")
        else:
            new_password = input("Create a password: ")
            # Save it to the dictionary
            user_database[new_username] = new_password
            print(f"User '{new_username}' registered successfully!")
            
    # --- OPTION 2: LOG IN ---
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        
        # Check if the username exists AND if the password matches the value stored
        if username in user_database and user_database[username] == password:
            print(f"Login successful! Welcome back, {username}.")
        else:
            print("Invalid username or password. Please try again.")
            
    # --- OPTION 3: DISPLAY USER COUNT ---
    elif choice == "3":
        # len() counts how many items are inside the dictionary
        total_users = len(user_database)
        print(f"Total registered users: {total_users}")
        
    # --- OPTION 4: EXIT ---
    elif choice == "4":
        print("Goodbye!")
        break # This stops the 'while' loop and ends the program
        
    else:
        print("Invalid choice. Please type a number from 1 to 4.")