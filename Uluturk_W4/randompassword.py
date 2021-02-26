'''
Developer: Ömer ULUTÜRK
Date: 24.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement


As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.

Acceptance Criteria:
Password length must be 10 characters long. It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages. The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
'''

import random
import string


def random_password():
    lower = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
    upper = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    punc = ''.join(random.choice(string.punctuation) for i in range(2))
    digits = ''.join(random.choice(string.digits) for i in range(2))
    password = list(lower + upper + punc + digits)
    random.shuffle(password)
    password = "".join(password)
    print(password)


random_password()
