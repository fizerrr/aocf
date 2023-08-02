import requests
import json

# Dane w formacie JSON
json_data = '''
{
  "departureAirportIataCode": "KRA",
  "outboundDepartureDateFrom": "2023-08-04",
  "market": "en-gb",
  "adultPaxCount": "1",
  "outboundDepartureDateTo": "2023-08-04",
  "outboundDepartureTimeFrom": "00:00",
  "outboundDepartureTimeTo": "23:59"
}
'''

# Konwersja danych JSON na słownik w Pythonie
data = json.loads(json_data)

# Zmienne dla parametrów URL
departure_airport = data['departureAirportIataCode']
departure_date_from = data['outboundDepartureDateFrom']
market = data['market']
adult_pax_count = data['adultPaxCount']
departure_date_to = data['outboundDepartureDateTo']
departure_time_from = data['outboundDepartureTimeFrom']
departure_time_to = data['outboundDepartureTimeTo']

# Tworzenie parametrów URL zmiennych
url_var = (
    f"?departureAirportIataCode={departure_airport}"
    f"&outboundDepartureDateFrom={departure_date_from}"
    f"&market={market}"
    f"&adultPaxCount={adult_pax_count}"
    f"&outboundDepartureDateTo={departure_date_to}"
    f"&outboundDepartureTimeFrom={departure_time_from}"
    f"&outboundDepartureTimeTo={departure_time_to}"
)

url_main = "https://www.ryanair.com/api/farfnd/v4/oneWayFares"

url = url_main + url_var

response = requests.request("GET", url)

print(response.text)
