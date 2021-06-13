import random
import string

character=string.ascii_letters+string.digits+string.punctuation
print(character)


character=string.ascii_letters+string.digits+string.punctuation
print(character)

pass_length=int(input("Enter length of password : "))
password=""

for i in range(pass_length+1):
    password+=random.choice(character)

print("Password ",password)

# or USING JOIN

password1=''.join(random.choice(character)for i in range(pass_length+1))

print("Password ",password1)
