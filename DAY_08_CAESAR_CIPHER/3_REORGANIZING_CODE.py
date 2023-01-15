alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(message,shift_by,direct):
  output_text=""
  for letter in message:
    position = alphabet.index(letter)
    if direct=="encode":
      new_position=(position+shift)%26           
    elif direct=="decode":
      new_position=(position-shift)%26
    output_text+=alphabet[new_position]
  print(f"The {direct}d text is {output_text}")
      

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(message=text,shift_by=shift,direct=direction)