#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pass_letters = str("")
# for nr_letter in range(1,nr_letters+1):
#   nr_letter = random.randint(0,len(letters)-1)
#   pass_letters =  pass_letters + letters[nr_letter]
# pass_symbols = str("")
# for nr_symbol in range(1,nr_symbols+1):
#   nr_symbol = random.randint(0,len(symbols)-1)
#   pass_symbols =  pass_symbols + symbols[nr_symbol]
# pass_numbers = str("")
# for nr_number in range(1,nr_numbers+1):
#   nr_number = random.randint(0,len(numbers)-1)
#   pass_numbers = pass_numbers + str(numbers[nr_number])
# print(pass_letters+pass_symbols+pass_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_letters = str("")
for nr_letter in range(1,nr_letters+1):
  nr_letter = random.randint(0,len(letters)-1)
  pass_letters =  pass_letters + letters[nr_letter]
pass_symbols = str("")
for nr_symbol in range(1,nr_symbols+1):
  nr_symbol = random.randint(0,len(symbols)-1)
  pass_symbols =  pass_symbols + symbols[nr_symbol]
pass_numbers = str("")
for nr_number in range(1,nr_numbers+1):
  nr_number = random.randint(0,len(numbers)-1)
  pass_numbers = pass_numbers + str(numbers[nr_number])
print(pass_letters+pass_symbols+pass_numbers)
pw = pass_letters+pass_symbols+pass_numbers
pw = list(pw)
print(pw)
pass_final = str("")
for char in range(1,len(pw)+1):
  nr_char = random.randint(0,len(pw)-1)
  pass_final =  pass_final + str(pw[nr_char])
  pw.pop(nr_char)
print(pass_final)
