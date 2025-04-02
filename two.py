import os

def vulnerable_function(user_input):
    os.system(user_input)

user_input = input("Enter a command: ") 
vulnerable_function(user_input)  
