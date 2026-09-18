# Simple dictionary example

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 84000000},
    "France": {"capital": "Paris", "population": 68000000},
    "Canada": {"capital": "Ottawa", "population": 38000000},
}

print("Country Capitals: ", country_capitals)
print(country_capitals["Germany"])

country_capitals["Italy"] = {"capital": "Rome", "population": 59000000}
print(country_capitals["Italy"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)