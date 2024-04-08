def password_checker(password, difficulty):
    if difficulty == "1":
        if len(password) >= 6:
            return "Successful! Password meets the Easy complexity requirements.\n"
        else:
            return "\n INVALID. Password must be at least 6 characters long.\n"

    elif difficulty == "2":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) \
                and any(char.isdigit() for char in password):
            return "Successful! Password meets the Medium complexity requirements.\n"
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("\n INVALID.Password must be at least 8 characters long.\n")
            if not any(char.isupper() for char in password):
                feedback.append("\n INVALID.Password must contain at least one uppercase letter.\n")
            if not any(char.islower() for char in password):
                feedback.append("\n INVALID.Password must contain at least one lowercase letter.\n")
            if not any(char.isdigit() for char in password):
                feedback.append("\n INVALID.Password must contain at least one digit.\n")
            return "\n".join(feedback)

    elif difficulty == "3":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) \
                and any(char.isdigit() for char in password) \
                and any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password):
            return "Successful! Password meets the Hard complexity requirements.\n"
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("\n INVALID.Password must be at least 8 characters long.\n")
            if not any(char.isupper() for char in password):
                feedback.append("\n INVALID.Password must contain at least one uppercase letter.\n")
            if not any(char.islower() for char in password):
                feedback.append("\n INVALID.Password must contain at least one lowercase letter.\n")
            if not any(char.isdigit() for char in password):
                feedback.append("\n INVALID.Password must contain at least one digit.\n")
            if not any(char in "\n INVALID. !@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password):
                feedback.append("Password must contain at least one special character (!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~).\n")
            return "\n".join(feedback)

    elif difficulty.lower() == "4":
        return "Exiting the password checker.\n"

    else:
        return "Invalid selection. \nChoose a difficulty level: \n 1. Easy \n 2. Medium \n 3. Hard\n 4. Exit\n \n Please input here: "


# Game loop
while True:
    print("Please enter level of difficulties:\n")
    difficulty_choice = input("Choose a difficulty level: \n 1. Easy \n 2. Medium \n 3. Hard\n 4. Exit\n \n Please input here: ")
    
    if difficulty_choice.lower() == "4":
        break
    
    if not difficulty_choice.isdigit() or int(difficulty_choice) not in [1, 2, 3, 4]:
        print("Invalid selection. \nChoose a difficulty level: \n 1. Easy \n 2. Medium \n 3. Hard\n 4. Exit\n  \n Please input here: ")
        continue

    user_password = input("Enter your password: ")

    # Test the password checker
    print(password_checker(user_password, difficulty_choice))
