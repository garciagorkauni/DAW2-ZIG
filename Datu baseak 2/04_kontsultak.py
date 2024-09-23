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

    # Get and show clients whose name is José or Luis
    try:
        query = '''SELECT Name, Surname FROM Client WHERE Name = 'José' OR Name = 'Luis' ORDER BY Name, Surname'''
        cursor.execute(query)
        results = cursor.fetchall()
        print("José edo Luis izeneko bezoreak:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Arazo bat egon da lehenengo kontsulta egiterakoan: {err}")

    # Get and show name and tlf of client whose age is btwn 45 and 50
    try:
        query = '''SELECT Name, Tlf FROM Client WHERE TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) BETWEEN 45 AND 50 ORDER BY TIMESTAMPDIFF(YEAR, BirthDate, CURDATE())'''
        cursor.execute(query)
        results = cursor.fetchall()
        print("45 eta 50 arteko adineko bezeroak:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Arazo bat egon da bigarren kontsulta egiterakoan: {err}")

    # Get and show clients without tlf
    try:
        query = '''SELECT Name, Surname FROM Client WHERE Tlf IS NULL'''
        cursor.execute(query)
        results = cursor.fetchall()
        print("Telefono gabeko bezeroak:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Arazo bat egon da hirugarren kontsulta egiterakoan: {err}")

    # Get and show products whos stock is < 5
    try:
        query = '''SELECT Name FROM Product WHERE Stock < 4'''
        cursor.execute(query)
        results = cursor.fetchall()
        print("Stock-a 4 baino gutxiago duten produktuak:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Arazo bat egon da laugarren kontsulta egiterakoan: {err}")

    # Get and show products whose price is < 200
    try:
        query = '''SELECT Name, Description, ProductImage FROM Product WHERE UnityPrice < 200'''
        cursor.execute(query)
        results = cursor.fetchall()
        print("200 euro baino gutxiago balio duten produktuak:")
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Arazo bat egon da bosgarren kontsulta egiterakoan: {err}")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
