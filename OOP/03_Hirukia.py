# Object class
class Hirukia:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def printLargestSide(self):
        print("Alde luzeena {} unitate neurtzen du.".format(max([self.side1, self.side2, self.side3])))
    
    def printType(self):
        sides = [self.side1, self.side2, self.side3]
        equalSides = len(set(sides))
        
        if equalSides == 1:
            print('Hirukia aldeberdina da.')
        elif equalSides == 2:
            print('Hirukia isoszelea da.')
        else:
            print('Hirukia eskalenoa da.')


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
    # Ask sides to the user
    side1 = ask_number('Sartu lehenengo aldearen luzera: ')
    side2 = ask_number('Sartu bigarren aldearen luzera: ')
    side3 = ask_number('Sartu hirugarren aldearen luzera: ')
    
    # Initialize Hirukia objet
    hirukia = Hirukia(side1, side2, side3)

    # Use Hirukia object printer methods
    hirukia.printLargestSide()
    hirukia.printType()

if __name__ == "__main__":
    main()
