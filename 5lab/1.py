import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def invert_case(password):
    return password.swapcase()

passwords = [generate_password() for i in range(5)]

inverted_passwords = list(map(invert_case, passwords))

print("Оригинальные пароли:", passwords)
print("Пароли с инвертированным регистром:", inverted_passwords)