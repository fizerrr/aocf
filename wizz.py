import requests,json
from cookie import return_cookie 


url = "https://be.wizzair.com/18.1.0/Api/asset/farechart"

cookie = return_cookie(url)

payload = {
    "isRescueFare": False,
    "adultCount": 1,
    "childCount": 0,
    "dayInterval": 7,
    "wdc": False,
    "isFlightChange": False,
    "flightList": [
        {
            "departureStation": "TIA",
            "arrivalStation": "VIE",
            "date": "2023-08-07"
        }
    ]
}
headers = {
    "cookie": f"{cookie}",
    "Host": "be.wizzair.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://wizzair.com/",
    "Content-Type": "application/json;charset=utf-8",
    "X-RequestVerificationToken": "86a198e5cfcc41148c9f4d615994afaf",
    "Content-Length": "188",
    "Origin": "https://wizzair.com",
    "Connection": "keep-alive",
    "Cookie": f"{cookie}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}

response = requests.request("POST", url, json=payload, headers=headers)

#print(response.text)

response = requests.request("POST", url, json=payload, headers=headers)


class FlightData:
    def __init__(self, outbound_flights, return_flights, show_prices):
        self.outbound_flights = outbound_flights
        self.return_flights = return_flights
        self.show_prices = show_prices

class Flight:
    def __init__(self, departure_station, arrival_station, price, price_type, date, class_of_service, has_mac_flight):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.price = price
        self.price_type = price_type
        self.date = date
        self.class_of_service = class_of_service
        self.has_mac_flight = has_mac_flight

# Parsowanie danych jako obiekt JSON
input_data = json.loads(response.text)

# Tworzenie obiektów klasy Flight na podstawie danych wejściowych
outbound_flights = []
for flight_data in input_data["outboundFlights"]:
    flight = Flight(
        departure_station=flight_data["departureStation"],
        arrival_station=flight_data["arrivalStation"],
        price=flight_data["price"],
        price_type=flight_data["priceType"],
        date=flight_data["date"],
        class_of_service=flight_data["classOfService"],
        has_mac_flight=flight_data["hasMacFlight"]
    )
    outbound_flights.append(flight)

# Tworzenie obiektu klasy FlightData
flight_data_obj = FlightData(
    outbound_flights=outbound_flights,
    return_flights=input_data["returnFlights"],
    show_prices=input_data["showPrices"]
)

# Przykładowe użycie
print("Liczba lotów wychodzących:", len(flight_data_obj.outbound_flights))
print("Czy pokazywać ceny:", flight_data_obj.show_prices)

