import random
import string


def generate_short_url(length: int = 10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))