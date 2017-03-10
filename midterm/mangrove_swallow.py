if __name__ == '__main__':
    countries = set()

    with open('world_cities.csv', 'r') as f:
        for line in f:
            city, country = line.split(',')
            countries.add(country.lower().replace('\n', ''))

    with open('mangrove_swallow.txt', 'r') as f:
        text = f.read().lower()

    print('The Mangrove Swallow can probably be found in:')
    for country in countries:
        if country in text:
            print(country.title())