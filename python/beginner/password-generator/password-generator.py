import random
import string

def generate_password(length):
    #Defining the characters to use

    chars_list = string.ascii_letters + string.digits + string.punctuation

    #Empty string for password
    password = ""

    #Looping 'length' number of times and picking random character for each position
    for _ in range(length):
        random_char = random.choice(chars_list)
        password += random_char

    return password

if __name__ == "__main__":
    print ("--- Welcome to the password generator ---")

    while True:
        try:
            #Lets ask the user to input password length.
            len_input = input("Enter the desired password length: ")
            password_length = int(len_input)

            if password_length <= 4:
                print ("Enter a positive integer greater than 3")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number")

    #Finally we can generate the password
    generated_pw = generate_password(password_length)
    print (generated_pw)