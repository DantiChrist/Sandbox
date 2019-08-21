password = input("Enter password: ")
password_length = len(password)
while password_length <= 5:
    password = input("Enter password: ")
    password_length = len(password)
print(password_length * "*")