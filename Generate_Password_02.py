
# Generate Password 02

import string
import random

alpha = string.ascii_letters
symbol = string.punctuation
numbers = string.digits

collection = alpha + symbol + numbers

length = input("length: ")

passwords = "".join(random.sample(collection, int(length)))

print(passwords)