def base_string():
    # The user must enter a value
    base_string = input("Entrer une valeur:")
    print("Valeur : " + base_string)
    return base_string


def list_ascii(base_string):
    list_ASCII = []
    for character in base_string:
        list_ASCII.append(ord(character))
    print(list(base_string))
    print(list_ASCII)
    return list_ASCII


def list_bin(list_ASCII):
    # List of characters converted to Binary
    list_bin = []
    for i in list_ASCII:
        list_bin.append(bin(int(i))[2:].zfill(8))
    # Display list format Binary
    print(list_bin)
    return list_bin


def character_bin(list_bin):
    # String of raw binary characters
    character_bin = ''.join(list_bin)
    print(character_bin)
    return character_bin


def list_bin_formatted(character_bin):
    # n = length of one block
    n = 6
    # list formatted with 6 digits in each block
    list_bin_formatted = [character_bin[i:i + n] for i in range(0, len(character_bin), n)]
    print(list_bin_formatted)
    return list_bin_formatted


def lastElement(list_bin_formatted):
    # list with 6 digits on the last element
    lastElement = list_bin_formatted[-1].ljust(6, "0")
    list_bin_formatted[-1] = lastElement
    print(list_bin_formatted)
    return list_bin_formatted


def list_dec(list_bin_formatted):
    # binary list to integer conversion
    list_dec = []
    for i in list_bin_formatted:
        list_dec.append(int(str(i), 2))
    print(list_dec)
    return list_dec


if __name__ == '__main__':
    base_string = base_string()
    list_ASCII = list_ascii(base_string)
    list_bin = list_bin(list_ASCII)
    character_bin = character_bin(list_bin)
    list_bin_formatted = list_bin_formatted(character_bin)
    list_bin_formatted = lastElement(list_bin_formatted)
    list_dec(list_bin_formatted)
