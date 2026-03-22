from datetime import datetime
import random
import string
def generate_random_number(min, max):
    return random.randint(min, max)
def generate_random_string(length=255):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))