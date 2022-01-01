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

# Write your code below this line 👇

picks = [rock, paper, scissors]

user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

computer = random.randint(0, 2)

print("""Rules:
      Rock wins against scissors
      Scissors win against paper
      Paper wins against rock""")


print("You chose:")
if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(picks[user])

    print("Computer chose:")
    print(picks[computer])

    if user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw")
