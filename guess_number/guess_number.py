from art import logo
import random
def guess_the_number():
  computer_number = random.randint(1, 100)
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  def attempt_counts():
    if difficulty == "easy":
      guesses = 10
    elif difficulty == "hard":
      guesses = 5
    return guesses
  def checkpoint():
    guesses = attempt_counts()
    game_over = False
    while guesses > 0 and game_over == False:
      print(f"You have {guesses} attempts remaining to guess the number.")
      user_guess = int(input("Make a guess: "))
      if user_guess == computer_number:
        print(f"You got it! The answer was {computer_number}")
        game_over = True
      elif user_guess < computer_number:
        print("Too low.")
        guesses -= 1
      else:
        print("Too high.")
        guesses -= 1
    if guesses == 0:
      print("You've run out of guesses, you lose.")
  checkpoint()
guess_the_number()
