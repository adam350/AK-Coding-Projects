import random
import string

def generate_password(length):
# define character sets to be used in password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

# create a password string by randomly selecting characters from each set
    password = ""
    password += random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(digits)
    password += random.choice(special_characters)

# add more characters until the password string reaches its desired length
    for i in range(length - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

# shuffle the passwords to increase randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password

password = generate_password(1)
print(password)