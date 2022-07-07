alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(input_text, input_shift):
  crypto = ""
  index = []
  for letter in input_text:
    index += [alphabet.index(letter)]
  for number in index:
    if number+input_shift < 26:
      crypto += alphabet[number+input_shift]
    else:
      while input_shift > 26:
        input_shift = input_shift - 26  
      new_shift = (number+input_shift)-26
      crypto += alphabet[new_shift]
  print(f"The encoded text is {crypto}")
def decrypt(input_text, input_shift):
  decrypt = ""
  index = []
  for letter in input_text:
    index += [alphabet.index(letter)]
  for number in index:
    if input_shift < 26:
      decrypt += alphabet[number-input_shift]
    else:
      while input_shift >= 26:
        input_shift = input_shift - 26
      new_shift = (number-input_shift)+26
      decrypt += alphabet[new_shift]
  print(f"The decoded text is {decrypt}")
if direction == "encode":
    encrypt(text, shift) 
elif direction == "decode":
    decrypt(text,shift)
