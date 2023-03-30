import string

def generator():
    specialChar = string.punctuation
    allChar = "These are the generated Special characters: ", specialChar
    return allChar
generator()
