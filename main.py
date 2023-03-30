#convert letters to upper cass
import random
import string
#Generate Strings from A-Z
def generate_strings():
    alph = string.ascii_letters
    return alph
def generate_numbers():
    nums = string.digits
    return nums

#generate special Characters
def generate_special_char():
    chars = string.punctuation
    return chars


#body of my codes
for i in range(3):
    pass_struc = random.choice(generate_strings()) + random.choice(generate_numbers())
    random_chars = random.choice(generate_special_char())
    pass_generated = pass_struc + random_chars
    print(pass_generated, end="")

