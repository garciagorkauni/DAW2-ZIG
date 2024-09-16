def edit_visits(PARAMETER):
    # Open the fjle to work with it
    try:
        with open('Fitxategien ariketak/bisitak.txt', 'r') as file:
            # Read the file an save its value
            counter = int(file.readline().strip())
    except:
        counter = 0

    if PARAMETER == 'G':
        counter += 1
    elif PARAMETER == 'K' and counter > 0:
        counter -= 1

    # Save and return the final counter
    with open('Fitxategien ariketak/bisitak.txt', 'w') as file:
        file.write(str(counter))
        return counter
    
def main():
    # Define the parameter
    PARAMETER = 'G'

    # Show the result to the user
    print('Parametroa {} izanda, kontadorearen balioa {} da.'.
    format(PARAMETER, edit_visits(PARAMETER)))

if __name__ == "__main__":
    main()