import requests,json



url = "https://be.wizzair.com/18.1.0/Api/asset/farechart"


payload = {
    "isRescueFare": False,
    "adultCount": 1,
    "childCount": 0,
    "dayInterval": 5,
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
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}



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



input_data = json.loads(response.text)

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

return_flights = []
for flight_data in input_data["returnFlights"]:
    flight = Flight(
        departure_station=flight_data["departureStation"],
        arrival_station=flight_data["arrivalStation"],
        price=flight_data["price"],
        price_type=flight_data["priceType"],
        date=flight_data["date"],
        class_of_service=flight_data["classOfService"],
        has_mac_flight=flight_data["hasMacFlight"]
    )
    return_flights.append(flight)

# Creating FlightData object
flight_data_obj = FlightData(
    outbound_flights=outbound_flights,
    return_flights=return_flights,
    show_prices=input_data["showPrices"]
)


print("Number of outbound flights:", len(flight_data_obj.outbound_flights))
print("Number of return flights:", len(flight_data_obj.return_flights))
print("Should show prices:", flight_data_obj.show_prices)


if flight_data_obj.outbound_flights:
    first_flight = flight_data_obj.outbound_flights[0]
    print(f"First outbound flight - From: {first_flight.departure_station}, To: {first_flight.arrival_station}, Price: {first_flight.price}, Date: {first_flight.date}")
