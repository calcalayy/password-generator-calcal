import random
import time

letters = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "-", "+", "=", "_", "f", "F", "g", "G", "h", "H", "[", "]", "I", "i", "j", "k", "K"]

# use * operator when printing to do all at once

print("Here is your password:")

time.sleep(2)

random.shuffle(letters)
first_chars = letters[0:8]
print(*first_chars)
