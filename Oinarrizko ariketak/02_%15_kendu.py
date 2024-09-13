def main():
    # Set some values
    DISCOUNT = 0.15

    # Ask to the user for a num
    while True:
        try:
            num = float(input("Sartu ezazu zenbaki bat: "))
            break
        except:
            print('Zure erantzuna ez du balio, saiatu berriz...')
            pass

    # Print the result
    print("%15a kenduta, emaitza: {}".format(num - (num*DISCOUNT)))

if __name__ == "__main__":
    main()