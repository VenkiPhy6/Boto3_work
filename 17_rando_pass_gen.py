import random as rd

pass_length=int(input("What length do you want the password to be?: "))
valid_characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

random_pass="".join(rd.choice(valid_characters) for i in range(pass_length))
print(random_pass)