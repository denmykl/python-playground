import random

letters_list = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM,.;!@#$%^&*?"

password_length = 20

letters_count = len(letters_list)
result = ""

counter = 0
while counter < password_length:

    random_number = random.randrange(0, password_length)
    result += letters_list[random_number]

    counter += 1

print(result)
