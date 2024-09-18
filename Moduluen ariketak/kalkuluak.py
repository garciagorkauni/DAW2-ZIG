from eragiketak import batu, kendu, bidertu, zatitu

def ask_number():
    while True:
            try:
                number = int(input("Zure aukera: "))
                return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def main():
    while True:
        # Print the menu
        print('''Aukeratu bat:
            1. Zenbakiak batu
            2. Zenbakiak kendu
            3. Zenbakiak biderkatu
            4. Zenbakiak zatitu
            5. Irten''')
        
        # Ask the user for the selected option
        option = ask_number()
        
        num1 = input('Lehenengo zenbakia: ')
        num2 = input('Bigarren zenbakia: ')
        
        if option == 1:
            print(batu(num1, num2))
        elif option == 2:
            print(kendu(num1, num2))
        elif option == 3:
            print(bidertu(num1, num2))
        elif option == 4:
            print(zatitu(num1, num2))
        elif option == 5:
            print('Programa itxi egingo da.')
            break
        else:
            print('Zure aukera ez da egokia.')

if __name__ == "__main__":
    main()
