def username():
    username = input("Username: ")
    print(f"Your username is {username}, correct?")
    return username

def age():
    age = input("Age: ")
    print(f"You are {age} year(s) old, correct?")
    return age

def confirm(func):
    x = func()
    while True:
        conf = input("Y / N: ").upper()

        if conf == 'Y':
            break
        elif conf == 'N':
            x = func()
        else:
            print("Invalid response, please retry")

    return x


user_name = confirm(username)
user_age = confirm(age)
print("Confirmation accepted")
print(f"""
Username: {user_name}
Age: {user_age}
""")
