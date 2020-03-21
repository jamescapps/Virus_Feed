import requests
import json
import pyfiglet


# Latest worldwide data
latest_response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/latest')
# By country
country_response = requests.get('https://pomber.github.io/covid19/timeseries.json')
# Gives back data for within Country
regional_response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=US')

title = pyfiglet.figlet_format('Virus Feed', font='slant')
print(title)

user_input = input('World, Country, or Region?: ')

# World numbers
if user_input.lower() == 'world':
    res = json.loads(latest_response.text)
    for key, value in res.items():
        print('Confirmed cases: ' + "{:,}".format(value['confirmed']))
        print('Deaths: ' + "{:,}".format(value['deaths']))
        print('Recovered: ' + "{:,}".format(value['recovered']))

# Numbers by country
if user_input.lower() == 'country':
    which_country = input('Enter the country: ')
    res = json.loads(country_response.text)
    for key, value in res.items():
        if key == which_country.title() or key == which_country.upper():
            print(key)
            print(value[-1]['date'])
            print('Confirmed cases: ' + "{:,}".format(value[-1]['confirmed']))
            print('Deaths: ' + "{:,}".format(value[-1]['deaths']))
            print('Recovered: ' + "{:,}".format(value[-1]['recovered']))

