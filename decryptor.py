# create decrypting program thru character substitution
# lists of vowels
english_vowels = ['a', 'e', 'i', 'o', 'u']
encrypted_vowels = ['*', '&', '#', '+', '!']
# ask input from user
encrypted_text = input('Enter a string to decrypt: ')
# placeholder variable
decrypted_text = 'The plain text: ' + '\033[33m' 
# main code
# print result