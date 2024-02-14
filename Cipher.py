import Cipher_arts
#encrpytion and decryption
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']

#creating the cipher function
def ceaser_cipher(letter,shift_amount,code_direction):
    cipherText=""
    if code_direction=="decode":
      shift_amount*=-1
    elif code_direction=="encode":
      shift_amount*=1
    else:
      print("Wrong input.")

    for char in letter:
      if char in alphabets:
        position=alphabets.index(char)
        new_index = position + shift_amount
        new_letter=alphabets[new_index]
        cipherText+=new_letter
      else:
        cipherText+=char
        
    print(f'Here is the {direction}d text: {cipherText}')

ceaser_logo=Cipher_arts.logo

end_encryption=True
while end_encryption: 
  print(ceaser_logo)
  direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your messsage:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift=shift % 26
  
#function output
  ceaser_cipher(letter=text,shift_amount=shift,code_direction=direction)
  
  result =input("Type 'yes' if you want to go again.Otherwise type 'no'.\n").lower()

  if result =='yes':
    end_encryption=True
  else:
    end_encryption=False
  