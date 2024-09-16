def read_data():
    # Open the fjle to work with it
    data = []
    with open('Fitxategien ariketak/jendea.txt', 'r') as file:
        # Read the file line by line
        for line in file.readlines():

            # Save each line data in a dict
            line_dict = {}
            line_dict['id'] = line.split(';')[0]
            line_dict['name'] = line.split(';')[1]
            line_dict['surname'] = line.split(';')[2]
            line_dict['birth'] = line.split(';')[3]

            data.append(line_dict)
        
        # Return the result list
        return data
    
def main():

    # Show the result to the user
    for line in read_data():
        print('{}. {} {} - {} '.format(
            line['id'], line['name'], line['surname'], line['birth']), end='')

if __name__ == "__main__":
    main()