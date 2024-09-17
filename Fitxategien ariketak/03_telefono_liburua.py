def find_phone(name):
    # Read the file and create it if necessary
    with open('Fitxategien ariketak/telefonoak.txt', 'a+') as file:
        # Read the file line by line
        file.seek(0)
        for line in file.readlines(0):
            if line.split('-')[0].strip().upper() == name.upper():
                return line.split('-')[1]
        return 'Ez dago holako bezerorik'        

def delete_phone(name):
    # Read the file and create it if necessary
    new_book = ''
    with open('Fitxategien ariketak/telefonoak.txt', 'a+') as file:
        # Save the file of the content without the selected client
        file.seek(0)
        for line in file.readlines():
            if line.split('-')[0].strip().upper() == name.upper():
                pass
            else:
                new_book += line
        
    
    with open('Fitxategien ariketak/telefonoak.txt', 'w') as file:
        file.write(new_book)
    
    return 'Erabiltzailea ondo ezabatu da'

def save_phone(name, number):
    # Read the file and create it if necessary
    with open('Fitxategien ariketak/telefonoak.txt', 'a+') as file:
        file.write('{} - {}\n'.format(name, number))
    return 'Zenbakia ondo gorde da'

def main():
    while True:
        # Print the menu
        print('''Aukeratu bat:
            1. Bezeroaren telefonoa bilatu
            2. Bezeroaren telefonoa ezabatu
            3. Bezeroaren telefonoa gehitu
            4. Irten''')
        
        # Ask the user for the selected option
        option = 0
        while True:
            try:
                option = int(input("Zure aukera: "))
                break
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass
        
        if option == 1:
            name = input('Sartu bezeroaren izena: ')
            print(find_phone(name))
        elif option == 2:
            name = input('Sartu bezeroaren izena: ')
            print(delete_phone(name))
        elif option == 3:
            name = input('Sartu bezeroaren izena: ')
            number = 0
            while True:
                try:
                    number = int(input("Sartu telefono zenbakia: "))
                    break
                except:
                    print('Zure erantzuna ez du balio, saiatu berriz..')
                    pass
            print(save_phone(name, number))
        elif option == 4:
            print('Programa itxi egingo da.')
            break
        else:
            print('Zure aukera ez da egokia.')


if __name__ == "__main__":
    main()