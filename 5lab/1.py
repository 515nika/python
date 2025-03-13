import random
import string

def generate_passwords(count, length=8):
    characters = string.ascii_letters + string.digits
    for i in range(count):
        password = ''.join(random.choice(characters) for i in range(length))
        yield password

def invert_case(password):
    return password.swapcase()

password_generator = generate_passwords(5)

pass_w = list(password_generator)
inverted_passwords = list(map(invert_case, pass_w))

print("Оригинальные пароли:", pass_w)
print("Пароли с инвертированным регистром:", inverted_passwords)
