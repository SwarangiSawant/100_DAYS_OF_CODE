alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
  new_text=""
  for letter in plain_text:
    position=alphabet.index(letter)
    new_position=(position+shift)%26
    new_text+=alphabet[new_position]
  print(f"The encoded text is {new_text}")

    ##HINT: How do you get the index of an item in a list:    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
  #Here if we put only (position+ shift) then when it comes z position would become 25+5=30 and this would give an error Out of index in order to avoid it and loop back we use(position+shift)%26 so here it becomes(30%26=4 and we will get e)
  
  #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text,shift_amount=shift)