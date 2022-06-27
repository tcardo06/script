# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_value(name):
    a_string = input("Entrer une valeur:")

    ASCII_values = []
    for character in a_string:
        ASCII_values.append(ord(character))
    print(list(a_string))
    print(ASCII_values)

if __name__ == '__main__':
    print_value('PyCharm')
