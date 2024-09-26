# Object class
class Pertsona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPertsona(self):
        print('{} {} urte ditu'.format(self.name, self.age))

# Method for asking user an integer num >= 0
def ask_number(prompt):
    while True:
            try:
                number = int(input(prompt))
                if number >= 0:
                    return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def main():
    # Ask the user for pertsona data
    name = input('Sartu pertsonaren izena: ')
    age = ask_number('Sartu pertsonaren adina: ')

    # Initialize Pertsona object
    pertsona = Pertsona(name, age)

    # Use Ikaslea print method
    pertsona.printPertsona()

    # Read object attributes
    print('Adinez nagusia!') if pertsona.age >= 18 else print('Adinez txikikoa...')

if __name__ == "__main__":
    main()
