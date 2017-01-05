import random
import string

def generate_password(length):
    password = ''
    for i in range(length):
        password += (chr(random.randint(33, 125)))
    print password


generate_password(6)
generate_password(10)
