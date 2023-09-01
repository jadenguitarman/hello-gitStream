# Initialize hardcoded username and password
USERNAME = 'admin'
PASSWORD = 'password123'

def authenticate(username, password):
    """
    Authenticate user based on username and password.
    """
    if username == USERNAME and password == PASSWORD:
        return True
    return False

def main():
    print("Welcome to the Authentication System.")

    # Prompt user for username and password
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Check if authentication is successful
    if authenticate(username_input, password_input):
        print("Authentication successful. Welcome!")
    else:
        print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()
