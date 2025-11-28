import random

random_number = random.randint(1,100)

while True:
    user_number = int(input("Your number: "))
    if 1 <= user_number <= 100:
        if random_number > user_number:
            print("More")
        elif random_number < user_number:
            print("Less")
        else:
            print(f"You guessed the number: {random_number}")
            break
    else:
        print("1 - 100")