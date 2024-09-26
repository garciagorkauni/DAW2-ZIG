class Bezero:
    def __init__(self, name, surname):
        # Initialize the attributes of the class
        self.name = name
        self.surname = surname
        self.total = 0

    def sum_money(self, amount):
        # Add a certain amount to the total balance
        self.total += amount
        print('{}€ sartu dira {} {} bezeroaren kontutik.'.format(amount, self.name, self.surname))

    def rest_money(self, amount):
        # Subtract a certain amount from the total balance
        self.total -= amount
        print('{}€ atera dira {} {} bezeroaren kontutik.'.format(amount, self.name, self.surname))

    def total_money(self):
        # Return the current total balance of the customer
        print('{} {} bezeroaren kontuan {}€ daude.'.format(self.name, self.surname, self.total))

class Bankua:
    def __init__(self):
        # Initialize the list of Bezero objects and the registry dictionary
        self.bezeroak = []
        self.registry = {}

    def add_bezero(self):
        # Get customer details from the user
        name = input('Sartu bezeroaren izena: ')
        surname = input('Sartu bezeroaren abizena: ')
        total = ask_float('Sartu kontuaren dirua: ')

        # Create a new Bezero object and add it to the list
        new_bezero = Bezero(name, surname, total)
        self.bezeroak.append(new_bezero)
        print('{} {} bezeroa gehitu da.'.format(name, surname))

    def bezero_sum_money(self):
        # Get necessary details from the user
        name = input('Sartu bezeroaren izena: ')
        surname = input('Sartu bezeroaren abizena: ')
        amount = ask_float('Sartu kantitatea: ')
        date = input('Sartu data (YYYY-MM-DD): ')

        # Find the customer and add money
        bezero = self.find_bezero(name, surname)
        if bezero:
            bezero.sum_money(amount)

            # Update the registry for the given date
            if date in self.registry:
                self.registry[date] += amount
            else:
                self.registry[date] = amount
        else:
            print('{} {} bezeroa ez da topatu.'.format(name, surname))

    def bezero_rest_money(self):
        # Get necessary details from the user
        name = input('Sartu bezeroaren izena: ')
        surname = input('Sartu bezeroaren abizena: ')
        amount = ask_float('Sartu kantitatea: ')
        date = input('Sartu data (YYYY-MM-DD): ')

        # Find the customer and rest money
        bezero = self.find_bezero(name, surname)
        if bezero:
            bezero.rest_money(amount)

            # Update the registry for the given date
            if date in self.registry:
                self.registry[date] -= amount
            else:
                self.registry[date] = amount
        else:
            print('{} {} bezeroa ez da topatu.'.format(name, surname))

    def get_day_registry(self):
        # Get the date from the user
        date = input('Sartu data (YYYY-MM-DD): ')

        # Display the total money deposited on the given date
        if date in self.registry:
            print('{} eguneko diru sarrerak: {}€.'.format(date, self.registry[date]))
        else:
            print('{} egunean ez daude diru sarrerarik.'.format(date))

    def find_bezero(self, name, surname):
        # Helper method to find a customer by name and surname
        for bezero in self.bezeroak:
            if bezero.name.lower() == name.lower() and bezero.surname.lower() == surname.lower():
                return bezero
        return None

# Method to ask the user for a valid number >= 0
def ask_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number >= 0:
                return number
        except ValueError:
            print('Sartu baliozko zenbaki bat.')

def ask_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
        except ValueError:
            print('Sartu baliozko zenbaki bat.')

def main():
    # Initialize the Bankua object
    bankua = Bankua()

    # Show the menu to the user in a loop
    while True:
        # Print the menu
        print('''
        Aukeratu bat:
        1. Bezeroa sortu
        2. Bezero moduan sartu
        3. Egun bateko diru sarrerak kontsultatu
        4. Irten
        ''')

        # Ask the user for the selected option
        option = ask_int('Sartu zure aukera: ')

        if option == 1:
            # Create a new customer (Bezeroa sortu)
            bankua.add_bezero()

        elif option == 2:
            # Enter as a customer (Bezero moduan sartu)
            name = input('Sartu bezeroaren izena: ')
            surname = input('Sartu bezeroaren abizena: ')
            bezero = bankua.find_bezero(name, surname)

            if bezero:
                while True:
                    # Print sub-menu for customer operations
                    print('''
                    Aukeratu bat:
                    1. Dirua sartu
                    2. Dirua atera
                    3. Dirua kontsultatu
                    4. Atzera
                    ''')
                    customer_option = ask_int('Sartu zure aukera: ')

                    if customer_option == 1:
                        # Deposit money
                        amount = ask_int('Sartu sartu nahi duzun diru kantitatea: ')
                        date = input('Sartu data (YYYY-MM-DD): ')
                        bankua.bezero_sum_money()  # Reuse the function to deposit money
                    elif customer_option == 2:
                        # Withdraw money
                        amount = ask_int('Sartu atera nahi duzun diru kantitatea: ')
                        date = input('Sartu data (YYYY-MM-DD): ')
                        bankua.bezero_rest_money()  # Reuse the function to withdraw money
                    elif customer_option == 3:
                        # Check balance
                        bezero.total_money()
                    elif customer_option == 4:
                        # Go back to main menu
                        break
                    else:
                        print('Aukera ez da zuzena.')

            else:
                print('{} {} bezeroa ez da topatu.'.format(name, surname))

        elif option == 3:
            # Consult daily deposits
            bankua.get_day_registry()

        elif option == 4:
            # Exit the program
            print('Programatik irteten...')
            break

        else:
            print('Aukera ez da zuzena.')

if __name__ == "__main__":
    main()

