import argparse
import logging


logging.basicConfig(level=logging.INFO)
logging.info('This will be logged')

base_string = argparse.ArgumentParser()
base_string.add_argument("string", help="string to test",type=str)
base_string = base_string.parse_args()
print("The string is : " + base_string.string)

list_ASCII = []
for character in base_string.string:
    list_ASCII.append(ord(character))

# Display list
print(list(base_string.string))

# Display list format Ascii
print(list_ASCII)

# List of characters converted to Binary
list_bin = []
for i in list_ASCII:
    list_bin.append(bin(int(i))[2:].zfill(8))

# Display list format Binary
print(list_bin)

# String of raw binary characters
character_bin = ''.join(list_bin)
print(character_bin)

# n = length of one block
n = 6

# list formatted with 6 digits in each block
list_bin_formatted = [character_bin[i:i + n] for i in range(0, len(character_bin), n)]
print(list_bin_formatted)

# list with 6 digits on the last element
lastElement = list_bin_formatted[-1].ljust(6, "0")
list_bin_formatted[-1] = lastElement
print(list_bin_formatted)
