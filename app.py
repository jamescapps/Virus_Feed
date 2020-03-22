import requests
import json
import pyfiglet


# Latest worldwide data
latest_response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/latest')
# By country
country_response = requests.get('https://pomber.github.io/covid19/timeseries.json')
# Gives back data for within Country
regional_response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=US')

country_found = True
state_found = True

title = pyfiglet.figlet_format('Virus Feed', font='slant')
print(title)

while True:
    done = False
    state_found = True
    user_input = input('World, Country, or States?: ')

    # World numbers
    if user_input.lower() == 'world':
        res = json.loads(latest_response.text)
        for key, value in res.items():
            print('Confirmed cases: ' + "{:,}".format(value['confirmed']))
            print('Deaths: ' + "{:,}".format(value['deaths']))
            print('Recovered: ' + "{:,}".format(value['recovered']))
            break
        # Check another
        check_another = input('Check something else?: (y) (n)')
        if check_another == 'y':
            continue
        elif check_another == 'n':
            print('Wash your hands! Goodbye!')
            exit()

    while True:
        # Numbers by country
        if not country_found:
            print('Country not found')
        if done:
            break

        if user_input.lower() == 'country':
            which_country = input('Enter the country: ')
            res = json.loads(country_response.text)
            for key, value in res.items():
                if key == which_country.title() or key == which_country.upper():
                    country_found = True
                    print(key)
                    print(value[-1]['date'])
                    print('Confirmed cases: ' + "{:,}".format(value[-1]['confirmed']))
                    print('Deaths: ' + "{:,}".format(value[-1]['deaths']))
                    print('Recovered: ' + "{:,}".format(value[-1]['recovered']))

                    # Check another
                    check_another = input('Check something else?: (y) (n)')
                    if check_another == 'y':
                        done = True
                        break
                    elif check_another == 'n':
                        print('Wash your hands! Goodbye!')
                        exit()
                else:
                    country_found = False
                    continue
                break

        # Numbers for states
        while True:
            if done:
                break
            if not state_found:
                print('State not found')
            if user_input.lower() == 'states':
                res = json.loads(regional_response.text)
                which_state = input('Enter name of state: ')
                for key, value in res.items():
                    for item in value:
                        if isinstance(item, dict):
                            for k, v in item.items():
                                if v == which_state.title():
                                    print(v)
                                    print('Confirmed cases: ' + "{:,}".format(item['latest']['confirmed']))
                                    print('Deaths: ' + "{:,}".format(item['latest']['deaths']))
                                    print('Recovered: ' + "{:,}".format(item['latest']['recovered']))

                                    # Check another
                                    check_another = input('Check something else?: (y) (n)')
                                    if check_another == 'y':
                                        done = True
                                        break
                                    elif check_another == 'n':
                                        print('Wash your hands! Goodbye!')
                                        exit()
                                else:
                                    state_found = False
                                    continue
                                break
                break

