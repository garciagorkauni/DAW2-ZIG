import datetime

def main():
    # Ask the user for birth date
    while(True):
        try:
            user_date = input('Sartu jaiotze-data AAAA-MM-DD formatoan: ').split('-')
            birth_date = datetime.date(int(user_date[0]), int(user_date[1]), int(user_date[2]))
            break
        except Exception:
            print('Ez duzu informazioa ondo sartu...')

    # Print birth-date weekday
    print('Zure jaiotzea asteko {}. eguna izan zen'.format(birth_date.isocalendar()[2]))

    # Calculate current date
    current_date = datetime.date.today()

    # Calculate time to birth date
    birthday = datetime.date(current_date.year, birth_date.month, birth_date.day)
    days_to_birth = (birthday-current_date).days

    if(days_to_birth > 0):
        print('{} egun falta dira zure urtebetetzerako!'.format(days_to_birth))
    elif(days_to_birth < 0):
        print('Zure urtebetetzea duela {} egun izan zen'.format(days_to_birth*(-1)))
    elif(days_to_birth == 0):
        print('Zure urtebetetzea gaur da!')


if __name__ == "__main__":
    main()
