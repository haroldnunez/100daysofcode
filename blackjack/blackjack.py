from art import logo
from replit import clear
import random
def blackjack():
  def deal():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
  restart_game = True
  more_cards = True
  while restart_game:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    if play_game == "y":
      print(logo)
      user_cards = []
      pc_cards = []
      for i in range (0,2):
        user_cards.append(deal())
        pc_cards.append(deal())
      while sum(pc_cards) < 17:
        pc_cards.append(deal())
      if sum(pc_cards) > 21:
        if 11 in pc_cards:
          pc_cards.remove(11)
          pc_cards.append(1)
      if sum(user_cards) > 21:
        if 11 in pc_cards:
          pc_cards.remove(11)
          pc_cards.append(1)
      print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
      print(f"   Computer's first card: {pc_cards[0]}")
      while more_cards:
        extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if extra_card == "y":
          user_cards.append(deal())
          if sum(user_cards) > 21:
            for card in range(len(user_cards)):
              if user_cards[card] == 11:
                user_cards[card] = 1
          if sum(user_cards) > 21:
            more_cards = False
          print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
          print(f"   Computer's first card: {pc_cards[0]}")
        else:
          more_cards = False
      print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
      print(f"   Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
      if sum(user_cards) > 21 and sum(pc_cards) > 21:
        print("You went over. You lose 😤")
      elif sum(user_cards) == sum(pc_cards):
        print("Draw 🙃")
      elif sum(pc_cards) == 21:
        print("Lose, opponent has Blackjack 😱")
      elif sum(user_cards) == 21:
        print("Win with a Blackjack 😎")
      elif sum(user_cards) > 21:
        print("You went over. You lose 😭")
      elif sum(pc_cards) > 21:
        print("Opponent went over. You win 😁")
      elif sum(user_cards) > sum(pc_cards):
        print("You win 😃")
      else:
        return "You lose 😤"
    else:
      restart_game = False
blackjack()
