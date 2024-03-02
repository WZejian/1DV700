import os
from random import randint
import matplotlib.pyplot as plt

# A list containning all the words in 'holy_grail'
home = os.getcwd()
path = home + '/holy_grail.txt'
line_lst = []
with open(path) as file:
    for line in file:
        line_lst.append(line.strip())
new = ''
for string in line_lst:
    for cha in string:
        new += cha
lst = new.split()


# A hash function returns a hash value of a string
def hs_val(string):
    sum = 0
    for e in string:
        sum += randint(0, ord(e))**2
    hs_val = sum % 256
    return hs_val


# A list contaning all the hash values of all string in holy_grail
hs_val_lst = []
for string in lst:
    hs_val_lst.append(hs_val(string))

# Graph for showing first property(uniformity)
plt.hist(hs_val_lst, bins=256)
plt.title('Uniformity')
plt.xlabel('Hash value in range 0 to 255')
plt.ylabel('Hash value frequency')
plt.show()


# 1000 tests with input different strings which only differ in one bit
text = "Unanswered questions"  # different strings based on this text string
hs_val_text = hs_val(text)
lst_text = [char for char in text]
hs_val_difference_lst = []
sum = 0
for i in range(1000):     # 1000 hash value differences between text and new_text changed 1 bit.
    # randomly choose a letter in the text and convert it to binary bits
    n = randint(0, len(text)-1)
    binary_converted = format(ord(text[n]), '08b')
    # randomly choose a bit position and change to 0 or 1 that is different from the original 
    lst = [b for b in binary_converted]
    m = randint(0, len(lst)-1)
    if lst[m] == '0':
        lst[m] = '1'
    else:
        lst[m] = '0'
    bit_changed_binary = ''.join(lst)
    # Convert the bit_changed_binary bits to a new symbol and then new text
    integer = int(bit_changed_binary, 2)
    char = chr(integer)
    lst_text[n] = char
    new_text = ''.join(lst_text)
    # A list containning 1000 different hash values between text and new text.
    hs_val_new_text = hs_val(new_text)
    hs_val_difference = hs_val_text - hs_val_new_text
    hs_val_difference_lst.append(hs_val_difference)

# A dictionary with keys of difference between based hash values and with values of frequency
hs_dic_differ = {}
for i in hs_val_difference_lst:
    if i not in hs_dic_differ:
        hs_dic_differ[i] = 0
    hs_dic_differ[i] += 1

# Show second property of hash function
plt.figure(2)
coordinates = sorted(hs_dic_differ.items())
x = [coordinates[n][0] for n in range(len(coordinates))]
y = [coordinates[m][1] for m in range(len(coordinates))]
plt.title('Hash value differences and its frequencyies')
plt.xlabel('Hash value differencies between based string and 1 bit-changed input string')
plt.ylabel('Hash value difference frequencies')
plt.plot(x, y)
plt.show()
