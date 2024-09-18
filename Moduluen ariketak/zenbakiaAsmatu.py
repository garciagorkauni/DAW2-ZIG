import math, random

def ask_number(prompt):
    while True:
            try:
                number = int(input(prompt))
                return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def irakurri_zenbakiak(min, max):
    try:
        num = random.randint(min, max)
        return num
    except:
        return 'Maximoa ezin da minimoa baino txikiagoa izan...'

def zenbakia_asmatu(num):
    attempts = 7

    while attempts > 0:
        user_num = ask_number('Zure aukera: ')

        if user_num > num:
            print('Asmatu beharreko zenbakia txikiagoa da.')
        elif user_num < num:
            print('Asmatu beharreko zenbakia handiagoa da.')
        elif user_num == num:
            return True

        attempts -= 1
        print('{} saiakera geratzen zaizkizu'.format(attempts))
    
    return False