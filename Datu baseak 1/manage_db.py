import mysql.connector
from db_utils import taulak_sortu, datuak_hasieratu, datuak_ezabatu, taulak_ezabatu, gehitu_ikaslea, nota_sartu, nota_aldatu, gehitu_ikasgaia, ezabatu_ikaslea

def ask_number(prompt):
    while True:
            try:
                number = int(input(prompt))
                return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def main():
    # Initialize the database connection
    dbConnect = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'Admin123',
        'database': 'testing'
    }
    connection = mysql.connector.connect(**dbConnect)

    # Create tables and show message to the user
    if taulak_sortu(connection):
        print('Taulak sortu dira.')

    # Fill tables and show message to the user
    if datuak_hasieratu(connection):
        print('Datuak ondo gorde dira')

    # Show the menu tho the user
    while True:
        # Print the menu
        print('''Aukeratu bat:
            1. Ikasle berri bat gehitu
            2. Ikasle bate ikasgai batean duen nota sartu
            3. Ikasle batek ikasgai batean duen nota aldatu
            4. Ikasgai berri bat sartu
            5. Ikasgai bat ezabatu
            6. Irten''')
        
        # Ask the user for the selected option
        option = ask_number('Sartu zure aukera: ')
        
        if option == 1:
            # gehitu_ikaslea
            # Ask user for kodea, izena, abizena
            code = ask_number('Sartu ikaslearen kodea (ezin da errepikatu): ')
            name = input('Sartu ikaslearen izena: ')
            surname = input('Sartu ikaslearen abizena: ')
            print(gehitu_ikaslea(connection, code, name, surname))

        elif option == 2:
            # nota_sartu
            # Ask user for nota, oharra, ikasle_kode, ikasgai_kode
            ikasle_code = ask_number('Sartu ikaslearen kodea: ')
            ikasgai_code = ask_number('Sartu ikasgaiaren kodea: ')
            mark = ask_number('Sartu nota: ')
            note = input('Sartu notaren oharra: ')
            print(nota_sartu(connection, ikasle_code, ikasgai_code, mark, note))

        elif option == 3:
            # nota_aldatu
            # Ask user for nota, oharra, ikasle_kode, ikasgai_kode
            ikasle_code = ask_number('Sartu ikaslearen kodea: ')
            ikasgai_code = ask_number('Sartu ikasgaiaren kodea: ')
            mark = ask_number('Sartu nota berria: ')
            note = input('Sartu notaren ohar berria: ')
            print(nota_aldatu(connection, ikasle_code, ikasgai_code, mark, note))

        elif option == 4:
            # gehitu_ikasgaia
            # Ask user for kodea, izena, maila, hizkuntza
            code = ask_number('Sartu ikasgaiaren kodea (ezin da errepikatu): ')
            name = input('Sartu ikasgaiaren izena: ')
            level = input('Sartu ikasgaiaren maila: ')
            language = input('Sartu ikasgaiaren hizkuntza: ')
            print(gehitu_ikasgaia(connection, code, name, level, language))

        elif option == 5:
            # ezabtu_ikaslea
            # Ask user for kodea
            code = ask_number('Sartu ikaslearen kodea: ')
            print(ezabatu_ikaslea(connection, code))

        elif option == 6:
            while True:
                # Print the menu
                print('''Programa itxi duzu, baino bukatu aurretik:
            1. Datu guztiak ezabatu
            2. Taula guztiak ezabatu
            3. Dena mantendu eta irten''')
                
                # Ask the user for the selected option
                option = ask_number('Sartu zure aukera: ')
                
                if option == 1:
                    datuak_ezabatu(connection)
                    print('Datuak guztiz ezabatu dira')
                    break
                elif option == 2:
                    taulak_ezabatu(connection)
                    print('Taula guztiak ezabatu dira')
                    break
                elif option == 3:
                    print('Datuak ez dira ezabatu')
                    break
                else:
                    print('Zure aukera ez da egokia.')
            break
        else:
            print('Zure aukera ez da egokia.')
            break

if __name__ == "__main__":
    main()
