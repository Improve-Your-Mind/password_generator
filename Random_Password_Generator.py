"""
In this script i would like to be able to ask the user how long their password should be.
    In later iterations i would like to be able to ask what characters they would like to use.
"""

# This is to import the random module as well as the string module
import random, string
# Comment to display who wrote the code
print('\nThis is a random password generator developed by Burnblade\n')


def main():
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    characters = [x for x in all_characters]

    # define user input
    pass_num = int(input('Please enter how many passwords to generate: '))
    pass_len = int(input('Please enter how long the password should be: '))

    # printing to screen the users randomly generated passwords
    print('\nYour randomly generated password is: \n')

    # for loop to generate the passwords
    for password in range(pass_num):
        passwords = ''
        for length in range(pass_len):
            passwords += random.choice(characters)

        print(passwords)


main()

