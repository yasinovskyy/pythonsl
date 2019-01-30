password = "secret"
user_passwd = input("Enter the password: ")
while user_passwd != password:
    print("Wrong...")
    user_passwd = input("Enter the password: ")
print("Congratulations!")
