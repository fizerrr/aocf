import csv

def search_airports_by_country(csv_file, country):
    airports = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['country'].lower() == country.lower():
                airports.append({
                    'code': row['code'],
                    'name': row['name'],
                    'city': row['city'],
                    'country': row['country'],
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude'])
                })

    return airports

