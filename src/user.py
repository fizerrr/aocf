from search import search_airports_by_country
from ryanair.ryanair import fetch_data
month = '8'
your_country = 'Poland'
where = 'Italy'

start_airports = search_airports_by_country(csv_file='data/airports.csv', country=your_country)

#output = fetch_data(start_airports[0][], departure_date_from, market, adult_pax_count, departure_date_to, departure_time_from, departure_time_to)

print(start_airports)



