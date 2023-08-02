import requests,json,csv

url = "https://be.wizzair.com/18.1.0/Api/asset/map"

querystring = {"languageCode":"en-gb"}

payload = ""
headers = {
    #"cookie": "_abck=8C1F842D2CCB8276570A624974EFDC04~-1~YAAQpGReaE94ebeJAQAAt1GztwqPV48iEIIFI%2B%2B2hZsTA4g67Ax4PRq6kHhETBw42cqL51mxXvpcGJ8ef%2BdImC62XPviig35Two%2BQWuGFMtiddM84QyrwOgwOR%2Fzq91GyaioORDLlMUciSywXOGCIDX6KO4Ea1FufI3AvPaCYYrPs54BWCT4vw7gPuGfefdUDYBHuckStW1efaEOlZsUZMa9rQ0ly8EUZmuSBfTQjRnRQj8cOTz%2FAhUQmxDjZYGqADrbZIoqybrwVsUCvezpyh58rxGFge5ZdIptXVNocgvsGdH8UOxgrwGypyGFsh6lP%2FSRa0zMzpsPJ6OBmCe%2FizR%2FufG7MUfdlVT6Rroq2c4YQhBHSLhbdrqCS1JrpEX7js2oTERs73T86nXk4642Gja3mZoKmUSAQT33EA4C3CPUR%2B4KYFmJub3mEslYs2coWvCMg4Im0xdtkS4tajFV~-1~-1~-1; RequestVerificationToken=565f0330284a454cadd16aac8dacc27a; bm_sz=3C5C201DCC34AC74FEADE9472EB2E9E7~YAAQpGReaFF4ebeJAQAAt1GztxQ8%2BRxY9Vfy5oda5B%2BLc%2FuSmQNK4TgySGN7PlByL5rdJp8NP4cUeQ3AD5ibVanrwfRJjnM7iBp7fQiKaEi7QR%2FkZsq02HnFS03ljSdZv4uoKACXfvrWdFN8gU%2F6tKonuwBAdUcMZqAin0BMQqJeJDFmAyPYFU9kkIXyG2WjNKui1qAd1WrRt5e7kEbQ7GOFf248c%2BSWoWSByrCJGKBzTLFQRydFXx%2BKmFfp%2FE%2BRBmPMccvDVNHHMyV%2F6CAkaGj4O3u%2BIvBAPgvMu21Vn9qNhBTpR2OKTnKTMw%2FBDGqojKiJQ59uzJPcGsRM1oqwpRULup%2BDKgZTOOoJ0q%2F%2FfLaortTDDJYyRLJ7zYa00w8uHamL%2BTwNVYQ5AglvUfNYzVgDWtRMtwnGdw%3D%3D~4338489~4604724",
    "Host": "be.wizzair.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://wizzair.com/en-gb/",
    "Origin": "https://wizzair.com",
    "Connection": "keep-alive",
    #"Cookie": "_abck=8C1F842D2CCB8276570A624974EFDC04~-1~YAAQpGReaEY6ebeJAQAA4oSxtwpok2KrVvit/ifXuJmv8CKo1f7dl3RLNvfIurTQIWg9gzfjl9X7NjeCiraeP5MI+L3Umhv85ZVLhwRPzhXOkEGkKJtSyRbNZV1BAS2xKJwp9PkigNfM6AO9p+NoWA1im6/kScuvaq3AWZXOXhsFPXNsho20JLrnSLf+A78Bt4tnT0pg3lptcsuyo1Tk4qZ6FgqLONROjFYLNwB/ZNzuA1716OUesZb7/kg1lW2AQMGK2FbtgglNePBDc9keyR5JKdFT/4xvpOFyRlxwTw56Auv5DynAmJzwysjnCO9BNkAQR6LG1uF75fkOvNKPS3XorOunSRp25GsVAapM0fdyRH8vRincwlamNSHTia9NrF3QiNhQDDoADlBNcJpN6Kzm75FBWf35+vXpCxawus5Rr4EqxTdZ12ah58vlYje5oICKBwA8B6cy17vX7jE=~-1~-1~-1; _gcl_au=1.1.1701106507.1690475860; _ga_G2EKSJBE0J=GS1.1.1691003996.4.0.1691004010.0.0.0; _ga=GA1.2.1255528815.1690475860; _pin_unauth=dWlkPU5qbGlNMk0wT0RndE1HUmtNUzAwTWpRekxUaGlZVFV0TlRrMFl6VmxaRGd6Wm1ObQ; _tt_enable_cookie=1; _ttp=bh-y0VOKUADBAEfBTZDgag3i0LE; _fbp=fb.1.1690475862272.476777185; ak_bmsc=D705D78C8CE3788969890FABF5358192~000000000000000000000000000000~YAAQpGReaK4xebeJAQAAQkWxtxRbwUyc86ECOCnsIdorYiAswKJhCx4kNqaAKmuPo7npuw2FSbeB3oC50ERgNeK06XlLGIKznzms9tgq8syLnH7Vor3g+WEUVTEULFqQ7fFgY+EQ3h97QDJiHC0x9UY/YXy9J1l7lFO7D+c3mm1wj4F1t8IdD81xdRlEw/J4GRy5pKaVZ8P0vJRRUBP/TInoAvIAQd9sCur5gb0La5JfLI/2fGIyDQrHOraeYB1nmSraHTd71Lp7862FFtcM7hDjviOPcHUrfb8hkpwfqLpJIxeBR+3IzU817rUKnkqvPw5BuE6Yg9CuPEyUZUfeE6PPz06hQdkKO0vFtHrr7lel0ru++DtYF3A+Mgt3/XXDBnlwuOO8IWkBxzW/L6FVZhpCJ2KL8ITJ0J9CoWws2lnPH1Z7ms/fQNcC4SlgbUXkWaILUQdYNesYK9KdaCeH7pOYOCf5G5ScfJIKJgBowXBffPZ8ja6SckjwfodYdapduhiFbm/FaLI3ToFMhS7CHYJ0Nss=; bm_sz=597FD70AF49B7942A38153BB47FE7711~YAAQpGReaCgxebeJAQAAk0GxtxSXhlGW5a3UWc6PUAL74pBotIxwvrOD+k6yyS0v0jwBQa/DwGkC/SpSG8qJmmGF8IGIcSeUUr77Yy66t4HLJ2btLb2WPu9qnvJF5eEJzLhCppQfNtf7M5t3brhmF1T/t0OP7bJBO/HBuncdnHVvpLcTRCorl22pxDeyT0c1IMbmr6eV59kWlX13ImrlLou5NShDOwNYLrZ63FhKPVhWdPZKf+Qd2RwYyRJE3jedg/DnVHr+6ofyXbDR1gbW/NX7SFJBp8a/5Z5CW3o0ALGUBwPjlbq9gRusatN42YAnJY1w+VIsaplYVXPRNNnJaYMfpNHmIuzMUkRZVdn/4sT7IAcZT6Rlow2q+K/ZaaAPJ8T6MKGyBrKN6/pIlBldnwbMKrTq7Zu1E/Arm0+CUbwWqDuq+OXbRaU=~3551297~3684166; bm_sv=E23BC98FA15CD49F70D4841FAF6FB947~YAAQpGReaG46ebeJAQAAGYaxtxQfChkqMg/znuhlaipKZKZWWwwopozXmAMcOyfLoMWWkJESCSmuWRI82igHyhGVXQl4++JRdtdr8HQj3td/xbfgh0UvDK1zDeO2JYjEBPXJb7Ql4VWboWYtwpHCZC1D9IDK0bj98imU7hdfrF+3A7gwYDKz6naVYHHMBD06ivSwAnxj/zREjnDg8yU/uFs+lBllYcG2ORn8L3K5VWL/EHYhywgdk+E9VJ2FvbQk/So=~1; ASP.NET_SessionId=clciqwsvh1ybsejh3mh2ohpd; RequestVerificationToken=ac4a2a8a93084a31bd247d2b0a4d3332; _gid=GA1.2.136972107.1691003997; _gat_gtag_UA_2629375_25=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    "X-RequestVerificationToken": "ac4a2a8a93084a31bd247d2b0a4d3332",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)



try:
    json_data = json.loads(response.text)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the response text.")


print(json_data['cities'][0])

flat_data = []
for city in json_data['cities']:
    flat_data.append({
        'iataCode': city.get('iataCode', ''),
        'name': city.get('name', ''),
        'shortName': city.get('shortName', ''),
        'countryCode': city.get('countryCode', ''),
    })

# Save the flattened data to CSV
csv_file = 'data/cities_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['iataCode', 'name', 'shortName', 'countryCode']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for city_data in flat_data:
        writer.writerow(city_data)

print(f"Data saved to {csv_file}")