import requests,json

url = "https://be.wizzair.com/18.1.0/Api/asset/farechart"

xd = 3

payload = {
    "isRescueFare": False,
    "adultCount": f'{xd}',
    "childCount": 0,
    "dayInterval": 3,
    "wdc": False,
    "isFlightChange": False,
    "flightList": [
        {
            "departureStation": "LUZ",
            "arrivalStation": "SPU",
            "date": "2023-09-07"
        }
    ]
}
headers = {
    "cookie": "bm_sv=90951F9B8E43FAAAC6D6ED6E606B489B~YAAQn2ReaCRHFq2JAQAAO8QsrRR2QC70TqUMX7i8OVoLc%2F5qmLWuKKSELCs93ow%2BO%2BDJOzSia%2Bh1Jdl857zq0OnwC%2F1RcbV%2FMfxnWyi%2BJ5EQndDNsqkPDWF7b3e4ieJoME36lBjXUahJJyM733csky1E0BRIdcOtDmkmIVQCS6CkkknRLaJDgCym7eRAqcIfcEE1l6xH1PrPeTAHQvElVkofHEJRXTMxUBeJ8ZtESyw1v0BVIr3fxI5znNXE0lThRDE%3D~1; _abck=8C1F842D2CCB8276570A624974EFDC04~-1~YAAQn2ReaBnpFa2JAQAAIGgorQowT2je9qDMMCbSKENcJix8ZZeXIwKRdaPQB%2BPv4fsr4K%2BSfGFdjGH3a0dwQ%2FykXKvbSNRq8413p2ktoDYHvvRcsAD1GWjI2zDdyT2BHqHttUnXy5fbqpUA6mKV6XY5ntZXELMeoFsabwzEfsLsMyooNaAl5H1Z1wS1RM6Hh6MpvsLu2Zy%2BmlrxGT7T6Z9X%2FK8p1WSxEX5m%2BR8FNCYFa7sZHf619kfSmmfAd81vINvrKBDv65BjB6oZyKhjbCEh8AQF0aGK8gBWRZk9%2BTsxSEsbtvgV3Qc%2BXgdw%2BapY7eK6YzgeTpbehoizqvdgITPUPQblePxisBTRyU6eRbEdbGS2C6ISprU0gDgoiRz%2FDPnauhmebda4uG2YdoySYABQCLogLD10bilXsofdKsOdhL%2FCAjCtlt5opqQ9DGTZdXpf3bSimoeKPmI%2B%2FbY%3D~0~-1~-1; ak_bmsc=E03DE7E41221E40D3834E16E2BFAA029~000000000000000000000000000000~YAAQn2ReaAM9Fq2JAQAAkigsrRSQzuvhqjxyyPiAr1H3qKcnkIzLxV2avsikjYphMy1GyLBhSn0VmH%2FP9QGTuC2rq8n2lBheUNIxNyTIJpZZKCDd3cQdjmhZx2u0hcmDuaPl%2Fb8jrF8DoJ8PGIrkczm1BtSkcOqRqCfztAcHn49dXVeAgqDtgIRljwjcprNO8SVmpaZzuuOEM95zOLc%2FwcPvOl2qHnsdWfJad5VSBvNwsYYXTQ6XfjdGuWQdFxlSnzLxR7b459%2FnzTQQY27wKuTLKKaPqM6XaUlG%2F7wD8DP3OntRwxpZbbsLhgyNoKpckOQ9rCP82Fkz7q6IYA%2Bg%2BsGssjRgKHYMBEFpWAOWnxCOlTSra6dyTNpu5MakasS8NJ4crvx4aEue6%2B7VwYYUX5c27lFedwBp2YgNLdpgIwXuPGFr%2Bi5YFvLpSo5DSPv34GjKIWoeWow5zr2UxE9UOteLuLigsPMR5ipYXiOuXE3BEqc87Wos8jZoIGRpHCjsN60zddjE7sRs0IueWEwlc8ZLn4aqoUTyHrTU8dM9UILwbji9dqg%3D; ASP.NET_SessionId=m0onmyv3yw04ernea4ajckee; RequestVerificationToken=e3bdba7ba8a440298b8ac798303b3ac1; bm_sz=AC736072DEC5BE80DA4767270859953F~YAAQn2ReaAI%2FFq2JAQAAzEUsrRRZFF3DVTrB4fJJUEFTXnkNQ4s6w%2FHKtwdiQFZynO8REoLdW6gQqHYBdN415eT0eogUo32xbUsI6IDvCxV%2FDSRN8ENPOksq9VyGkdCfJIQrNIPI0%2BNl6NO6vEX3KKs%2Bz1PW624X0RErbZhkOIyz3QK%2BH%2FvGCFTdM4JI0MWMZrFiW01R%2FO0bgbEiJRnsNdUys73yUvgS5YT%2BszszGaItJXiyd8btTXfDgkaPc1bSlr3kZvLUW%2FdaFsFeGRGXY6zVRymQV54Q0hShgf3RwD84mIiXkKt1z7iox%2BBWFpTjb374Xlzp9SNM73fVycBks5X1zFCj7Gu%2BnarWezrEO6vB87X4DH3RpHm8ySPwC1BPTAkLkaQUj%2Felw5QWrpozYynPeZshHTEI6WLSzK%2FknXhXFxuIyHZfnuoIeg%3D%3D~3687993~3617840",
    "Host": "be.wizzair.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://wizzair.com/en-gb",
    "Content-Type": "application/json;charset=utf-8",
    "X-RequestVerificationToken": "e9eb0aab9883492c8e65e240a58bbb5c",
    "Content-Length": "188",
    "Origin": "https://wizzair.com",
    "Connection": "keep-alive",
    "Cookie": "_abck=8C1F842D2CCB8276570A624974EFDC04~-1~YAAQpGReaEIKFa2JAQAA56cjrQqvzXroWcH3HaK/TfWrnOUAA9gzK2SsmlgLYCks9XM6Z9ESNW5OBuRFQrQFo2i95R2ntqQsYvWuSz6GYP8wa6GAaSUYSY8QelgYGiSRDO2Lx87r1EGtlfHpixWzzF5UAzQe+sS3FfQgO43K55Wi9Cz6ox8TK3t9tUQwl8GM2co54UMcNs5HNY/ELvu0ZgTbjb9xw16tgJpHvrkzzDUhVa9ss8Oh62bBhN2i1nLUOcrLBrodcPjjE1Y3VzlYXyuNU/gTSleGYP1/b+TRXNaGhuL+4YahAmK3+f7F4UHaELTl90FCyGhudYC1JfXePggqZCn96K8lDnsUhrLGjo6HMMuxlCZaAEhomwUUBqW17+MR1dp9xMa5gfvUolRAY38R+GE6lw6EJFqVHQPQ5I36QN+xvpCFcoHLNnONiokB3aRleVsc9FU+D+K0k5M=~-1~-1~-1; _gcl_au=1.1.1701106507.1690475860; _ga_G2EKSJBE0J=GS1.1.1690826850.2.1.1690826941.0.0.0; _ga=GA1.2.1255528815.1690475860; _pin_unauth=dWlkPU5qbGlNMk0wT0RndE1HUmtNUzAwTWpRekxUaGlZVFV0TlRrMFl6VmxaRGd6Wm1ObQ; _tt_enable_cookie=1; _ttp=bh-y0VOKUADBAEfBTZDgag3i0LE; _fbp=fb.1.1690475862272.476777185; ak_bmsc=E03DE7E41221E40D3834E16E2BFAA029~000000000000000000000000000000~YAAQpGReaHbSFK2JAQAAlTkirRTWZzj3VXEKAXRnsmJ4FrX5uawWwe0abKbZlSp8kX72XxCoRUBjABlQep7YEFDxG7LXXPwed/DZwYY/PiFX2YVzJ7KfxypvFbhS/WkrsMSiv8LRz5VwVP135ybC2GEh6mM6x+Wq4VDXoiUjvsa8esJxjLeNrDLlKM6bN4Fnd6vx3D1OMg82HVl95ewWgeIx9lqsiEVHV5pWLt6RQy/TttEPaIri3K1Gz0j/xnwQbyZ5xsOIF0Hj1IuXZuZq6hEJ6vH5zcm/q/2RNllQUBBAuLptSxXJJdnV+vCvHbvgcs3Mi8OP1Ml9/pmPLWeZ9VoFMILWHrKTTzW48rqJjm0dLn9KH7sVHfzhDujnB1wk3TKSEr+cHUOJpQlqeBvvWwxtBh1OV/UW1u28k5kxHlPWnR1WKvHG5Z+avtIdJucuyAaVGE+Pr3LH6OvhIe3VS9LaGfPYKU9vZuVkw85Ye2TR+imLHXDY4nQjwManCfQtV/Fw4lKi127wQAIxQQgc8v9rlMxA; bm_sz=3E54A579FC264143DBDA9C041AA3426B~YAAQpGReaCvSFK2JAQAAIzYirRQPxvdHyqbQlkwlCdcTjpV+PgN4dhUh867AqImIELxWCBNDChLVVnOKHN2BgLMXJvefT7LHHPzsIaoZ0P/kzIkJu+uXt8r6ZfL63R6mt6du4GfNUo3MgL+Z+92LWjD/enUaw8sKsTA94sLgXaIqLIuU8x7eFK+NGPaqD3+WiVHJnXPjjwzQP55ZLclBhEOnR2IE8lun72dLTBIN9T/g9PAFw1LJI0nffx9NELHo7Bc1mzXdFxQYNWye6YRTavRBWyXnsacSQBAqV5JL+AxGJhMrmVnqxKF/VZaixxDswTYnSEQskNF/fKxuNh3YkkXee8vegxv3q10PCBLjl4+pVQtUvxLw88PI/73rSLy2Ad5jyNkY02p+wMhxS8a6mfkVtSlW081fXrt4orH6+YkE/FT+qRiZ2QblKA==~3687221~3749697; bm_sv=90951F9B8E43FAAAC6D6ED6E606B489B~YAAQpGReaFoLFa2JAQAAGLAjrRSBBXiEeX/fGqV0vvxXHeDM9oZ32DAJNsWKYWKnLvXGEYCAeKaEMxe6618SfXGPuLGw1j/sgp50XBNmjyAw/suxDX2LiWrGZGaN3yAYJdDWICXnyt9cpF8L/J8ZzrreO3Nn4x5qTyMHa/yopfBrRGSJLWxJelOQtinYfXpjGQrbiCxECrIzo86X1FYc/NP/Q1B3j4oy22Y0r1B7oBrOnjPD2F3HuEdRER5Pgb9wJtc=~1; ASP.NET_SessionId=p1du5mvenllapqneifcr0myn; RequestVerificationToken=e9eb0aab9883492c8e65e240a58bbb5c; _gid=GA1.2.257359599.1690826851; _gat_gtag_UA_2629375_25=1",
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


#https://www.ryanair.com/api/farfnd/v4/oneWayFares?departureAirportIataCode=WAW&outboundDepartureDateFrom=2023-08-04&market=en-gb&adultPaxCount=1&outboundDepartureDateTo=2023-08-04&outboundDepartureTimeFrom=00:00&outboundDepartureTimeTo=23:59