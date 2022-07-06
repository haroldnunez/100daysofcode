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

#Write your code below this line 👇
import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >=3 and user <0:
  print("You typed an invalid number, you lose!")
else:
  computer = random.randint(1,2)
  rps = [rock, paper, scissors]
  print(rps[user])
  print("Computer chose:")
  print(rps[computer])
  if user == computer:
    print("It's a draw")
  elif user == 0 and computer == 2:
    print("You win")
  elif user == 2 and computer == 0:
    print("You lose")
  elif user < computer:
    print("You lose")
  elif user > computer:
    print("You win")
