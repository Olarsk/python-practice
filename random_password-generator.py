# import the random and the string module
import random
import string

# creat a list of the possible password characters
password_characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def random_password_generator():
    # get the user's desired password length
    password_length = int(input('Please your password length: '))

    # shuffling the characters to get a mixture
    random.shuffle(password_characters)

    # picking random characters from the list
    password = []
    for i in range(password_length):
        password.append(random.choice(password_characters))

    # shuffling the result
    random.shuffle(password)

    # to convert the list to string and print the password
    print('Your password is: ' + ''.join(password))


# calling the function
random_password_generator()
