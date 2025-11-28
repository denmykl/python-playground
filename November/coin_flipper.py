import random

while True:
    choice_str = ("Make your choice: \n1.Heads \n2.Tails \n(1/2): ")
    if choice_str in ('1', '2'):
        player_coin = int(choice_str) - 1
        break
    else:
        print("Enter 1 or 2")

coin_flip = random.randint(0, 1)

if coin_flip == 1:
    print("Result: Heads")
else:
    print("Result: Tails")

if player_coin == coin_flip:
    print("You Win")
else:
    print("You Lose")