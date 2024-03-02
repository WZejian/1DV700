import os
import math
import sys


# function to read plaintext or encrypted_text in a file
def read_text(text_path):
    with open(text_path, encoding='utf-8') as file:
        return file.read()


# function to output text
def output_text(text_path, text):
    with open(text_path, 'w', encoding='utf-8') as file:
        return file.write(text)


# function of encryption method of substitution(Caesar method)
def encrypt_subs(plaintext, key):
    sum = 0
    for e in key:
        sum += ord(e)
    key = sum % 26
    encrypted_text = ''
    for c in plaintext:
        if c.isupper():
            encrypted_text += chr((ord(c) + key-65) % 26 + 65)
        elif c.islower():
            encrypted_text += chr((ord(c) + key-97) % 26 + 97)
        else:
            encrypted_text += c
    return encrypted_text


# function of decryption method of substitution(Caesar method)
def decrypt_subs(encrypted_text, key):
    sum = 0
    for e in key:
        sum += ord(e)
    key = sum % 26
    decrypted_text = ''
    for c in encrypted_text:
        if c.isupper():
            decrypted_text += chr((ord(c) - key - 65) % 26 + 65)
        elif c.islower():
            decrypted_text += chr((ord(c) - key - 97) % 26 + 97)
        else:
            decrypted_text += c
    return decrypted_text


# function of encryption methond of transposition(columnar)
def encrypt_trans(plaintext, key):
    sum = 0
    for e in key:
        sum += ord(e)
    key = sum % 26
    no_columns = key
    no_rows = math.ceil(len(plaintext)//no_columns)
    sub_text = "&" * (no_columns - len(plaintext) % no_columns)
    plaintext += sub_text   # fill "&" in the empty buckets in the last row in order to index the plaintext

    # Add  each letter in the buckets  to the empty encrypted_text column by column
    encrypted_text = ""
    for i in range(no_columns):
        for j in range(no_rows):
            index = i + j * no_columns
            encrypted_text += plaintext[index]
    return encrypted_text


# function of decryption methond of transposition(columnar)
def decrypt_trans(encrypted_text, key):
    sum = 0
    for e in key:
        sum += ord(e)
    key = sum % 26
    length = len(encrypted_text)
    no_columns = math.ceil(length // key)
    no_rows = math.ceil(length // no_columns)
    sub_text = "&"*(no_columns-(length % no_columns))
    encrypted_text += sub_text   # fill "&" in the empty buckets in the last row in order to index the plaintext

    # Add  each letter in the buckets to the empty decrypted_text column by column
    decrypted_text = ""
    for i in range(no_columns):
        for j in range(no_rows):
            index = i + j * no_columns
            decrypted_text += encrypted_text[index]

    # remove the substitutes "&" from the text
    lst = []
    for s in decrypted_text:
        if s == '&':
            continue
        else:
            lst.append(s)
    return ''.join(lst)


home = os.getcwd()
plaintext_path = home + '/plaintext.txt'
encrypted_subs_path = home + '/encrypted_subs_text.txt'
decrypted_subs_path = home + '/decrypted_subs_text.txt'
encrypted_trans_path = home + '/encrypted_trans_text.txt'
decrypted_trans_path = home + '/decrypted_trans_text.txt'

# choose a encryption method and a key for users
encrypted_method = input("For encryption method of substition enter 'es', For encryption method of transposition enter 'et': ")
plaintext = read_text(plaintext_path)
if encrypted_method == 'es':
    key = input('Enter a key(no more than 8 bits): ')
    encrypted_text = encrypt_subs(plaintext, key)
    output_text(encrypted_subs_path, encrypted_text)
elif encrypted_method == 'et':
    key = input('Enter a key(no more than 8 bits): ')
    encrypted_text = encrypt_trans(plaintext, key)
    output_text(encrypted_trans_path, encrypted_text)
else:
    print('Please follow the instruction')
    sys.exit()

print('The plaintext file has been encrypted, please see the output of encrypted text')
print()

# choose a decryption method and a key for users
decrypted_method = input("For decryption method of substition you chose enter 'ds',"
                         "For decryption method of transposition you chose enter 'dt': ")
if decrypted_method == 'ds':
    encrypted_text = read_text(encrypted_subs_path)
    key = input('Enter a key the same as your encryption: ')
    decrypted_subs_text = decrypt_subs(encrypted_text, key)
    output_text(decrypted_subs_path, decrypted_subs_text)

elif decrypted_method == 'dt':
    encrypted_text = read_text(encrypted_trans_path)
    key = input('Enter a key the same as your encryption: ')
    decrypted_trans_text = decrypt_trans(encrypted_text, key)
    output_text(decrypted_trans_path, decrypted_trans_text)

else:
    print('Please follow the instruction')
    sys.exit()

print('The encrypted text file has been decrypted, please see the output of decrypted text')
