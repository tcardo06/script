# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_value(name):
    # The user must enter a value
    base_string = input("Entrer une valeur:")

    # List of characters converted to Ascii
    list_ASCII = []
    for character in base_string:
        list_ASCII.append(ord(character))

    # Display list
    print(list(base_string))

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


if __name__ == '__main__':
    print_value('PyCharm')
