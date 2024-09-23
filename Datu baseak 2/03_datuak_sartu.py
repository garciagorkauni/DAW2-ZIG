import mysql.connector
from datetime import datetime

def main():
    dbConnect = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'Admin123',
        'database': 'testing'
    }
    connection = mysql.connector.connect(**dbConnect)
    cursor = connection.cursor()

    # Data for the Client table (with omitted fields for default values)
    clients = [
        ('José', 'Fernández Ruiz', 'Estudio Cero', 'Gerente', 656789043, '1968-06-13'),
        ('Luis', 'Fernández Chacón', 'Beep', 'Dependiente', 675894566, '1982-05-24'),
        ('Antonio', 'Ruiz Gómez', 'Comar', 'Dependiente', 654345544, '1989-08-06'),
        ('Andrea', 'Romero Vázquez', 'Estudio Cero', 'Dependiente', 646765657, '1974-11-23'),
        ('José', 'Pérez Pérez', 'Beep', 'Gerente', 645345543, '1978-04-10')
    ]

    try:
        query = '''INSERT INTO Client (Name, Surname, Company, Position, Tlf, BirthDate) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.executemany(query, clients)
        connection.commit()
        print('Bezeroen datuak ondo kargatu dira.')
    except mysql.connector.Error as err:
        print(f'Arazo bat egon da bezeroen datuak kargatzerakoan: {err}')

    # Data for the Product table (unchanged)
    products = [
        ('NETGEAR switch prosafe', 'Switch 8 puertos GigabitEthernet', 125.0, 3, None),
        ('Switch SRW224G4-EU de Linksys', 'CISCO switch 24 puertos 10/100', 202.43, 2, None),
        ('Switch D-link', 'D-Link smart switch 16 puertos', 149.9, 7, None),
        ('Switch D-link', 'D-Link smart switch 48 puertos', 489.0, 4, None)
    ]

    try:
        query = '''INSERT INTO Product (Name, Description, UnityPrice, Stock, ProductImage) VALUES (%s, %s, %s, %s, %s)'''
        cursor.executemany(query, products)
        connection.commit()
        print('Produktuen datuak ondo kargatu dira.')
    except mysql.connector.Error as err:
        print(f'Arazo bat egon da produktuen datuak kargatzerakoan: {err}')

    # Data for the Purchase table (unchanged)
    purchases = [
        (1, 1, 2),
        (1, 2, 1),
        (2, 3, 1),
        (2, 4, 1),
        (3, 1, 2),
        (4, 2, 1),
        (5, 3, 3),
        (1, 4, 1),
        (1, 1, 2),
        (2, 2, 1),
        (3, 3, 4),
        (4, 4, 2),
        (5, 1, 1)
    ]

    try:
        query = '''INSERT INTO Purchase (client_id, product_id, quantity) VALUES (%s, %s, %s)'''
        cursor.executemany(query, purchases)
        connection.commit()
        print('Erosketen datuak ondo kargatu dira.')
    except mysql.connector.Error as err:
        print(f'Arazo bat egon da erosketen datuak kargatzerakoan: {err}')

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
