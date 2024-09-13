def hiriak_ordenatzen(population):
    # Define some variables
    result = list()
    cities_to_delete = list()

    # Find cities < 20000 to delete
    for city, people in population.items():
        cities_to_delete.append(city) if people < 200000 else None

    # Delete small cities
    [population.pop(city) for city in cities_to_delete]
    
    # Sort the dict and create the result list
    [result.append(item) for item in sorted(population, reverse=True)]

    return result

def main():
    # Define test values
    population = {'Soraluze': 5000, 'Bilbao': 350000, 'Donosti': 225000, 'Eibar': 25000}
    
    # Show the result to the user
    print(hiriak_ordenatzen(population))

if __name__ == "__main__":
    main()