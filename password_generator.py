#imports
import string #string.ascii_letters, string.digits, and string.punctuation
import secrets

#Ask user for length
def password_question ():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    password_length = input('How many characters would you like in your password? ')

    # Validate input: must be digits only (e.g., "12")
    while not password_length.isdigit():
        print("Please use a number")
        return
    
    length = int (password_length)

    # Sanity check
    if length <= 0:
        print("Please enter a number greater than 0.")
        return
    
    password = ""
    for i in range(length):
        password += secrets.choice(alphabet) #help from https://www.educative.io/answers/what-is-the-secretschoice-function-in-python
        return password

generated = password_question()
if generated is not None:
    print("Generated password:", generated)


#Check complexity


#Print password

print(password_question())