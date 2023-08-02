import requests
import json
import csv


url = "https://be.wizzair.com/18.1.0/Api/asset/map"


query_params = {"languageCode":"en-gb"}


headers = {
    "Host": "be.wizzair.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://wizzair.com/en-gb/",
    "Origin": "https://wizzair.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    "X-RequestVerificationToken": "ac4a2a8a93084a31bd247d2b0a4d3332",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}


response = requests.get(url, headers=headers, params=query_params)

try:
    json_data = json.loads(response.text)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the response text.")

prepared_data = []
for city in json_data['cities']:
    prepared_data.append({
        'code': city['iata'],
        'name': city['shortName'],
        'city': city['shortName'],
        'country': city['countryName'],
        'latitude': city['latitude'],
        'longitude': city['longitude'],
    })


csv_file_path = "data/cities.csv"


csv_headers = ["code", "name", "city", "country", "latitude", "longitude"]


try:
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()
        for row in prepared_data:
            writer.writerow(row)

    print(f"Dane zostały zapisane do pliku {csv_file_path}.")

except Exception as e:
    print(f"Wystąpił błąd podczas zapisu danych do pliku CSV: {e}")
