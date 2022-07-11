from IPython.core.display import clear_output
from art import logo
print(logo)
print("Welcome to the secret auction program.")

other_bidders = "yes"
bidders = {}
def auction(name, amount):
  name = name
  amount = amount
  bidders[name] = amount

while other_bidders == "yes":
  name = input("What is your name?\n")
  amount = int(input("What's your bid?\n"))
  auction(name, amount)
  other_bidders = input("Are there other bidders? Type 'yes' or 'no'.\n")
  clear_output()

find_max = max(bidders, key=bidders.get)
f"The winner is {find_max} with a bid of {bidders[find_max]}."
