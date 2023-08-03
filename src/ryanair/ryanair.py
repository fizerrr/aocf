import requests
import json

def fetch_data(departure_airport, departure_date_from, market, adult_pax_count, departure_date_to, departure_time_from, departure_time_to):
    
    url_main = "https://www.ryanair.com/api/farfnd/v4/oneWayFares"
    
    url_var = (
        f"?departureAirportIataCode={departure_airport}"
        f"&outboundDepartureDateFrom={departure_date_from}"
        f"&market={market}"
        f"&adultPaxCount={adult_pax_count}"
        f"&outboundDepartureDateTo={departure_date_to}"
        f"&outboundDepartureTimeFrom={departure_time_from}"
        f"&outboundDepartureTimeTo={departure_time_to}"
    )

    url = url_main + url_var

    response = requests.request("GET", url)
    
    return response.text


# Używając tej funkcji
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

data = json.loads(json_data)


departure_airport = data['departureAirportIataCode']
departure_date_from = data['outboundDepartureDateFrom']
market = data['market']
adult_pax_count = data['adultPaxCount']
departure_date_to = data['outboundDepartureDateTo']
departure_time_from = data['outboundDepartureTimeFrom']
departure_time_to = data['outboundDepartureTimeTo']

response = fetch_data(departure_airport, departure_date_from, market, adult_pax_count, departure_date_to, departure_time_from, departure_time_to)

print(response)
