import random
from art import logo
from art import vs
from game_data import data
def hl():
  user_score = 0
  def run(compare_A, compare_B):
    if user_score == 0:
      compare_A = {}
      compare_B = {}
      while compare_A == compare_B:
        compare_A = random.choice(data)
        compare_B = random.choice(data)
    else:
        while compare_A == compare_B:
          compare_B = random.choice(data)
    return compare_A, compare_B
  compare_A, compare_B = run("","")
  def guess():
    print(logo)
    if user_score > 0:
      print(f"You're right! Current score: {user_score}")
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}. {compare_A['follower_count']}")
    print(vs)
    print(f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.{compare_B['follower_count']}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    return user_guess
  user_guess = guess()  
  game_over = False
  while game_over == False:
    if user_guess == "A":
      if compare_A['follower_count'] > compare_B['follower_count']:
        user_score+=1
        compare_A = compare_B
        compare_A, compare_B = run(compare_A, compare_B)
        user_guess = guess()
      else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {user_score}")
    elif user_guess == "B":
      if compare_A['follower_count'] < compare_B['follower_count']:
        user_score+=1
        compare_A = compare_B
        compare_A, compare_B = run(compare_A, compare_B)
        user_guess = guess()
      else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {user_score}")
hl()
