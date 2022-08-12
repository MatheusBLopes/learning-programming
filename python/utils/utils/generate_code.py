from contextlib import ContextDecorator
import csv
from functools import partial
import json
import random
import re
import string
from datetime import datetime

def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))

def generate_code(prefix=None, length=32):
    prefix = prefix or ''
    random_length = length - len(prefix)
    if random_length <= 0:
        return prefix

    allowed = string.ascii_uppercase + string.digits
    random_string = get_random_string(length=random_length, allowed_chars=allowed)
    return '{}{}'.format(prefix, random_string)


generate_quiz = partial(generate_code, prefix='QUIZ', length=16)

print(generate_quiz(), datetime.now())