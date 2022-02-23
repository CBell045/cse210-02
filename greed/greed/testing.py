import random

text = random.choices('*' , '[]')   #chr(random.randint(33, 126))
assert text != '*' or '[]' , "shape is not being pulled"

print(text)