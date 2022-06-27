# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_value(name):
    base_string = input("Entrer une valeur:")

    list_ASCII = []
    for character in base_string:
        list_ASCII.append(ord(character))
    print(list(base_string))
    print(list_ASCII)

    list_bin = []
    for i in list_ASCII:
        list_bin.append(bin(int(i))[2:])
    print(list_bin)

if __name__ == '__main__':
    print_value('PyCharm')
