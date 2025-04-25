import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase