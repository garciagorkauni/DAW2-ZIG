def main():
    # Ask the user for the position
    while True:
        try:
            num = int(input("Sartu ezazu zenbaki oso bat: "))
            break
        except:
            print('Zure erantzuna ez du balio, saiatu berriz...')
            pass

    # Show the result to the user
    print("Bikoitia da?: {}".format(bool(not (num%2))))

if __name__ == "__main__":
    main()