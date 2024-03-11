def inverte_string(string):
    inverted_string = ''
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

# String a ser invertida
string = input("Digite uma string para inverter: ")

print("String invertida:", inverte_string(string))
