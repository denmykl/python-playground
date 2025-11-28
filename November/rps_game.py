import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if input_choice >= 3 or input_choice < 0:
    print("You typed an invalid number! Enter 0 or 1 or 2")
else:
    print("You chose:")
    print(game_images[input_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if input_choice == computer_choice:
        print("It's a draw")
    elif input_choice == 0 and computer_choice == 2:
        print("You win!")
    elif input_choice == 1 and computer_choice == 0:
        print("You win!")
    elif input_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose")