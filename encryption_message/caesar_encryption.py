from art import logo
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
restart = "yes"
while restart == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  def caesar(input_text, input_shift, direction):
      text_output = ""
      if direction == "decode":
          input_shift *= -1
      for char in input_text:
        if char not in alphabet:
          text_output += char
        elif char in alphabet:
          position = alphabet.index(char)
          text_output += alphabet[(position+input_shift)%26]
      print(f"Your text is {text_output}")
  caesar(input_text = text, input_shift = shift, direction = direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()    
