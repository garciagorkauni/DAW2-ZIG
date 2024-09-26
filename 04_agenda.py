# Object class
class Kontaktua:
    def __init__(self, name, tlf, mail):
        self.name = name
        self.tlf = tlf
        self.mail = mail
    
    def toString(self):
        return '{} ({}) - {}'.format(self.name, self.mail, self.tlf)

class Agenda:
    def __init__(self):
        self.kontaktuak = []

    def addKontaktua(self):
        # Ask user for contact data
        name = input('Idatzi kontaktuaren izena: ')
        tlf = ask_number('Idatzi kontaktuaren telefonoa: ')
        mail = input('Idatzi kontaktuaren posta elektronikoa: ')

        # Create Kontaktua object
        kontaktu_berria = Kontaktua(name, tlf, mail)

        # Save the object into Agenda object
        self.kontaktuak.append(kontaktu_berria)
    
        # Show success message to the user
        print('Hurrengo kontaktua agendan gorde da: {}'.format(kontaktu_berria.toString()))
    
    def showAgenda(self):
        print('Hauek dira zure agendako kontaktuak: ')
        for kontaktua in self.kontaktuak:
            print('\t- {}'.format(kontaktua.toString()))

    def findKontaktua(self, name):
        for kontaktua in self.kontaktuak:
            if kontaktua.name.lower() == name.lower():
                return kontaktua
    
    def editKontaktua(self, name):
        kontaktua = self.findKontaktua(name)

        # Show the menu tho the user
        while True:
            # Print the menu
            print('''Zein eremu aldatu nahi duzu:
                1. Izena
                2. Telefonoa
                3. Posta elektronikoa''')
            
            # Ask the user for the selected option
            option = ask_number('Sartu zure aukera: ')
            
            if option == 1:
                name_berria = input('Idatzi izen berria: ')
                kontaktua.name = name_berria

                print('Izena ondo aldatu da.')
                break

            elif option == 2:
                tlf_berria = ask_number('Idatzi telefono berria: ')
                kontaktua.tlf = tlf_berria

                print('Telefonoa ondo aldatu da.')
                break

            elif option == 3:
                mail_berria = input('Idatzi posta elektroniko berria: ')
                kontaktua.mail = mail_berria

                print('Posta elektroniko ondo aldatu da.')
                break

            else:
                print('Zure aukera ez da egokia.')
                break


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
    # Initialize Agenda object
    agenda = Agenda()

    # Show the menu tho the user
    while True:
        # Print the menu
        print('''Aukeratu bat:
            1. Gehitu kontaktua
            2. Inprimatu harremanetarako zerrenda
            3. Bilatu kontaktua
            4. Editatu kontaktua
            5. Irten''')
        
        # Ask the user for the selected option
        option = ask_number('Sartu zure aukera: ')
        
        if option == 1:
            agenda.addKontaktua()

        elif option == 2:
            agenda.showAgenda()

        elif option == 3:
            name = input('Sartu topatu nahi duzun kontaktuaren izena: ')
            try:
                print(agenda.findKontaktua(name).toString())
            except:
                print('Ez da {} izenarekin kontakturik aurkitu...'.format(name))

        elif option == 4:
            name = input('Sartu editatu nahi duzun kontaktuaren izena: ')
            agenda.editKontaktua(name)

        elif option == 5:
            break

        else:
            print('Zure aukera ez da egokia.')
            break

if __name__ == "__main__":
    main()