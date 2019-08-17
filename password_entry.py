"""Russell"""
MINIMUM_PASSWORD_LENGTH = 7
valid_password = False
while not valid_password:
    password = input("Enter password: ")
    if len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password is too short")
    else:
        valid_password = True

for i in range(len(password)):
    print("*", end="")
