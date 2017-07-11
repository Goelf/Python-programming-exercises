import random

# Password generator procedure
# Users need to input two numbers.
# The first is the number of password should be generated, the second is the length of the password.


def password_gen():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFG,./[]1234567890"
    choose_number = int(input("How many numbers of password you want?"))
    if choose_number == 0:
        print ("The minimum number of password is one!")
        raise SystemExit
    choose_length = int(input("How long of the password do you need?(minimum 8)"))
    if choose_length < 8:
        print("The minimum length of password is eight!")
        raise SystemExit
    password_list = []
    for number in range(choose_number):
        password = ""
        for i in range(choose_length):
            password += random.choice(char)
        password_list.append(password)
    return password_list

# Write the generated password to a file


def write_to_file(password_list):
    with open("D:\python\passwords.txt", "w") as f:
        for i in password_list:
            f.write(i+"\n")


write_to_file(password_gen())

