'''2. The Caesar cipher (also known as Caesar's code or Caesar shift) is one of the simplest and oldest encryption techniques. 
It is named after Julius Caesar, who reportedly used it to communicate secretly with his generals. The cipher is a type of substitution cipher, 
where each letter in the plaintext is shifted a certain number of places down the alphabet. 

    Write a program that encrypts text using Caesar Code, shifting each letter in the alphabet right one position.'''

    ###
    # Encrypts text using Caesar Code, shifting each letter
    # in the alphabet right one position
    #
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
        # read the character's code (use ord())
        code = ord(char)
        # add one to the character's code
        new_code = code+1
        # replace new character code with its
        # corresponding character (use chr())
        chr_code = chr(new_code)
        # add encrypted character to encrypted text
        encrypted_text += chr_code

print(plain_text)
print(encrypted_text)