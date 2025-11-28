import random

random_number = random.randint(1,100)

while True:
    user_number = int(input("Your number: "))
    if 1 <= user_number <= 100:
        if random_number > user_number:
            print("Больше")
        elif random_number < user_number:
            print("Меньше")
        else:
            print(f"Ты угадал загаданое число: {random_number}")
            break
    else:
        print("1 - 100")