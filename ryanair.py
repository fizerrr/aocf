import requests,json


json_data = '''
{
  "departureAirportIataCode": "WAW",
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

# Tworzenie parametrów URL zmiennych
url_var = (
    f"?departureAirportIataCode={data['departureAirportIataCode']}"
    f"&outboundDepartureDateFrom={data['outboundDepartureDateFrom']}"
    f"&market={data['market']}"
    f"&adultPaxCount={data['adultPaxCount']}"
    f"&outboundDepartureDateTo={data['outboundDepartureDateTo']}"
    f"&outboundDepartureTimeFrom={data['outboundDepartureTimeFrom']}"
    f"&outboundDepartureTimeTo={data['outboundDepartureTimeTo']}"
)


url_main = "https://www.ryanair.com/api/farfnd/v4/oneWayFares"




url = url_main + url_var


response = requests.request("GET", url)

print(response.text)