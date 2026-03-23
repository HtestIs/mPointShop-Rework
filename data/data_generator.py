from datetime import datetime
import random
import string
SAFE_SPECIAL = "!@#$%^&*"
def generate_random_number(min, max):
    return random.randint(min, max)
def generate_random_string(length=255):
    letters = string.ascii_letters + string.digits + random.choice(SAFE_SPECIAL)
    return ''.join(random.choices(letters, k=length))
def generate_random_string_missing_uppercase(length=255):
    data = [
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SAFE_SPECIAL),
    ]

    remaining = length - 3
    pool = string.ascii_lowercase + string.digits + SAFE_SPECIAL
    data += random.choices(pool, k=remaining)

    random.shuffle(data)
    return ''.join(data)
def generate_random_string_missing_lowercase(length=255):
    data = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(SAFE_SPECIAL),
    ]

    remaining = length - 3
    pool = string.ascii_uppercase + string.digits + SAFE_SPECIAL
    data += random.choices(pool, k=remaining)

    random.shuffle(data)
    return ''.join(data)
def generate_random_string_no_special(length=255):
    data = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    remaining = length - 3
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    data += random.choices(pool, k=remaining)

    random.shuffle(data)
    return ''.join(data)
def generate_random_string_no_digits(length=255):
    data = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(SAFE_SPECIAL),
    ]

    remaining = length - 3
    pool = string.ascii_lowercase + string.ascii_uppercase + SAFE_SPECIAL
    data += random.choices(pool, k=remaining)

    random.shuffle(data)
    return ''.join(data)