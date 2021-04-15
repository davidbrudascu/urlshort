import string, random

def generate_random():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(3))
    return random_string