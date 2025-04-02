import hashlib
import os

def authenticate_user():

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin123":
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed.")
        return False

def generate_new_api_key():
  try:
    user_input = input("Enter a  number: ")
    new_api_key = hashlib.sha256(str(user_input).encode()).hexdigest()
    print(f"Your new API key is: {new_api_key}")

  except Exception as e:
    print(f"Error evaluating the expression: {e}")

def main():
    if authenticate_user():
        generate_new_api_key()

if __name__ == "__main__":
    main()
