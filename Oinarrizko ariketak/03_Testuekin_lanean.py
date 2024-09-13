def main():
    # Ask to the user for a text
    text = input("Sartu ezazu testu bat: ")

    # Show the first char to the user
    print("Testuaren lehenengo karakterea: {}".format(text[0]))

    # Ask the user for the position
    while True:
        try:
            position = int(input("Sartu {} baino zenbaki positibo txikiago bat: ".format(len(text))))
            break
        except:
            print('Zure erantzuna ez du balio, saiatu berriz...')
            pass

    # Just in case users answer is not correct
    while position > len(text):
        position = int(input("Zure erantzuna ez du balio, saiatu berriro ({} baino txikiagoa): ".format(len(text))))

    # Show the result to the user
    print("Posizio horretan ({}) dagoen karakterea: {}".format(position, text[position-1]))

if __name__ == "__main__":
    main()