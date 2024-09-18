from zenbakiaAsmatu import irakurri_zenbakiak, zenbakia_asmatu

def ask_number(prompt):
    while True:
            try:
                number = int(input(prompt))
                return number
            except:
                print('Zure erantzuna ez du balio, saiatu berriz..')
                pass

def main():
    if zenbakia_asmatu(irakurri_zenbakiak(ask_number('MINIMOA: '), ask_number('MAXIMOA: '))):
        print('¡ZORIONAK, IRABAZI DUZU!')
    else:
        print('Oooooh... ez duzu irabazi...')

if __name__ == "__main__":
    main()
