import random
import string

charvalue = string.ascii_letters + string.digits + string.punctuation
password_len = 12



password = ""
for i in range(password_len):
    password += random.choice(charvalue)

print("your random password = ", password)

