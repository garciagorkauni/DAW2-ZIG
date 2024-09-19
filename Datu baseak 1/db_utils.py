import mysql.connector

def taulak_sortu(connection):
    cursor = connection.cursor()

    try:
        # Create ikasleak table
        query = '''CREATE TABLE Ikasleak (kodea int NOT NULL, izena text NOT NULL, abizena text NOT NULL, PRIMARY KEY(kodea))'''
        cursor.execute(query)

        # Create ikasgaiak table
        query = '''CREATE TABLE Ikasgaiak (kodea int NOT NULL, izena text NOT NULL, maila text NOT NULL, hizkuntza text NOT NULL, PRIMARY KEY(kodea))'''
        cursor.execute(query)

        # Create notak table
        query = '''CREATE TABLE Notak (nota int NOT NULL, oharra text NOT NULL, ikasgai_kodea int NOT NULL, ikasle_kodea int NOT NULL, FOREIGN KEY (ikasgai_kodea) REFERENCES Ikasgaiak(kodea), FOREIGN KEY (ikasle_kodea) REFERENCES Ikasleak(kodea))'''
        cursor.execute(query)

        return True
    
    except:
        return False

def datuak_hasieratu(connection):
    cursor = connection.cursor()

    try:
        # Fill ikasleak table
        query = 'INSERT INTO Ikasleak VALUES (%s, %s, %s)'
        data = [
            (1, 'Jon', 'Telleria'),
            (2, 'Aritz', 'Arruabarrena')
            ]
        cursor.executemany(query, data)
        connection.commit()

        # Fill ikasgaiak table
        query = 'INSERT INTO Ikasgaiak VALUES (%s, %s, %s, %s)'
        data = [
            (1, 'Informatika', 'Goi-maila', 'Euskera'), 
            (2, 'Matematika', 'Erdi-maila', 'Gaztelera')
            ]
        cursor.executemany(query, data)
        connection.commit()

        # Fill notak table
        query = 'INSERT INTO Notak VALUES (%s, %s, %s, %s)'
        data = [(8, 'Oso ondo', 1, 1),
                (4, 'Gutxi', 1, 2),
                (10, 'Bikain', 2, 1),
                (7, 'Oso ondo', 2, 1),
                ]
        cursor.executemany(query, data)
        connection.commit()
        return True
    
    except:
        return False

def taulak_ezabatu(connection):
    cursor = connection.cursor()
    
    try:
        query = 'DROP TABLE Ikasleak, Ikasgaiak, Notak'
        cursor.execute(query)
        return True
    
    except:
        return False

def datuak_ezabatu(connection):
    TABLES = ['Notak', 'Ikasleak', 'Ikasgaiak']
    cursor = connection.cursor()
    
    try:
        for table in TABLES:
            query = 'DELETE FROM {}'.format(table)
            cursor.execute(query)
            connection.commit()
        return True

    except:
        return False