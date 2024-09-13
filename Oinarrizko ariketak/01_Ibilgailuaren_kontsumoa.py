def main():
    # Ask to the user for the values
    while True:
        try:
            km = float(input("Eginiko kilometroak: "))
            break
        except:
            print('Zure erantzuna ez du balio, saiatu berriz...')
            pass

    while True:
        try:
            l = float(input("Gastatutako gasolina litroak: "))
            break
        except:
            print('Zure erantzuna ez du balio, saiatu berriz...')
            pass

    # Print the result
    print("Gasolina/km: {}".format(km/l))

if __name__ == "__main__":
    main()
