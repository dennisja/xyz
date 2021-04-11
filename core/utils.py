import string
import random

CHARACTER_SET = string.ascii_uppercase + string.digits + string.ascii_lowercase


def generate_random_code(length):
    code_characters = [random.choice(CHARACTER_SET) for each_index in range(length)]
    return "".join(code_characters)
