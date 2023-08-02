import csv
import json
import requests

class Airport:
    def __init__(self, code, name, city, country, coordinates):
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

def process_json_to_csv(url, filename):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code} received from server.")
        return

    try:
        json_data = json.loads(response.text)

        airports = []
        for item in json_data:
            coordinates = item.get('coordinates', {'latitude': None, 'longitude': None})
            city = item.get('city', {'name': None})
            country = item.get('country', {'name': None})
            airport = Airport(
                item.get('code'),
                item.get('name'),
                city.get('name'),
                country.get('name'),
                coordinates
            )
            airports.append(airport)

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['code', 'name', 'city', 'country', 'latitude', 'longitude']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for airport in airports:
                writer.writerow({
                    'code': airport.code, 
                    'name': airport.name,
                    'city': airport.city,
                    'country': airport.country,
                    'latitude': airport.coordinates['latitude'],
                    'longitude': airport.coordinates['longitude']
                })

    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the response text.")

url = "https://www.ryanair.com/api/views/locate/5/airports/en/active"
process_json_to_csv(url, 'data/airports.csv')
