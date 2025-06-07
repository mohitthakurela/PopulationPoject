import requests
import csv

url = "https://restcountries.com/v3.1/all?fields=name,capital,population"

try:
    response = requests.get(url)
    response.raise_for_status()
    countries_data = response.json()

    store_country = []

    for country in countries_data:
        store_country.append({
            "Name": country.get("name", {}).get("common", "Unknown"),
            "Population": country.get("population", 0)
        })

    sorted_countries = sorted(store_country, key=lambda x: x["Population"], reverse=True) 
    print(sorted_countries)

    def display_summary(store_country):
        total = len(store_country)
        total_population = sum(c["Population"] for c in store_country)
        avg_population = total_population / total if total else 0
        print("\n📊 Summary Statistics")
        print(f"Total Countries: {total}")
        print(f"Total Population: {total_population:,}")
        print(f"Average Population: {avg_population:,.2f}")


    display_summary(store_country)
    print("\n🌍 Top 5 Countries by Population")
    for index, country in enumerate(sorted_countries[:5], start=1):
        print(f"{index}. {country['Name']}: {country['Population']}")
    
    with open("top_5_country.csv", 'w', newline='') as file:
        wr = csv.writer(file)
        wr.writerow(['Rank','Name','Population'])
        for index, country in enumerate(sorted_countries[:5], start=1):
            wr.writerow([index,country['Name'], country['Population']])

except requests.exceptions.RequestException as e:
    print(f"❌{e}")

