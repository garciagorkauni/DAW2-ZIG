import mysql.connector

def main():
    # Initialize the database connection
    dbConnect = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'Admin123',
        'database': 'testing'
    }
    connection = mysql.connector.connect(**dbConnect)
    cursor = connection.cursor()

    # Create Client table (client_id)
    try:
        query = '''CREATE TABLE Client (client_id int NOT NULL, PRIMARY KEY(client_id))'''
        cursor.execute(query)
    
        print('Client taula ondo sortu da.')
    except:
        print('Arazo bat egon da Client taula sortzerakoan')

    # Create Product table (product_id)
    try:
        query = '''CREATE TABLE Product (product_id int NOT NULL, PRIMARY KEY(product_id))'''
        cursor.execute(query)
    
        print('Product taula ondo sortu da.')
    except:
        print('Arazo bat egon da Product taula sortzerakoan')
        
    # Create Purchase table (client_id, product_id, date, quantity)
    try:
        query = '''CREATE TABLE Purchase (client_id int NOT NULL, product_id int NOT NULL, quantity int NOT NULL, date DATE NOT NULL, FOREIGN KEY (client_id) REFERENCES Client(client_id), FOREIGN KEY (product_id) REFERENCES Product(product_id))'''
        cursor.execute(query)
    
        print('Purchase taula ondo sortu da.')
    except:
        print('Arazo bat egon da Purchase taula sortzerakoan')

if __name__ == "__main__":
    main()
