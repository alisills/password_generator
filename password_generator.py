#imports
import string #string.ascii_letters, string.digits, and string.punctuation
import secrets

#variables
alphabet = string.ascii_letters + string.digits + string.punctuation 
password = ''
password_length = input('How many characters would you like in your password? ')
length = range(int(password_length))

#Create 16 character password
for i in length:
    password +=str(''.join(secrets.choice(alphabet))) #help from https://www.educative.io/answers/what-is-the-secretschoice-function-in-python

#Ask user for length

#Generate password

#Check complexity

#Print password
print(password)