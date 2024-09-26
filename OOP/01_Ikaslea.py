# Object class
class Ikaslea:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def printIkasle(self):
        print('{}: {}'.format(self.name, self.mark))

# Method for asking user a num btwn 0-10
def ask_number(prompt):
    while True:
            try:
                number = float(input(prompt))
                if number >= 0 and number <= 10:
                    return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def main():
    # Ask the user for ikasle data
    name = input('Sartu ikaslearen izena: ')
    mark = ask_number('Sartu ikaslearen nota: ')

    # Initialize Ikaslea object
    ikaslea = Ikaslea(name, mark)

    # Use Ikaslea print method
    ikaslea.printIkasle()

    # Read object attributes
    print('Gaindituta!') if ikaslea.mark >= 5 else print('Ez du gainditu...')

if __name__ == "__main__":
    main()
