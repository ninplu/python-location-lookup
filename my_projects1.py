import urllib.request, urllib.parse
import json, ssl
import os 

#Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Service url for WeatherMap and API key
weather_url = 'https://api.openweathermap.org/data/2.5/weather'
#Service url for GeoCoding
geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
#API key
api_key = os.getenv('WEATHER_API_KEY')
if not api_key:
    raise RuntimeError('Please set the WEATHER_API_KEY environment variable')

#Functions for sending request into WeatherMap

def get_weather(lat: float, lon: float) -> dict: #Retrieving weather data from OpenWeatherMap API

    params = {
        'appid': api_key,
        'lat': lat,
        'lon': lon,
        'units': 'metric',
    }

    url = weather_url + '?' + urllib.parse.urlencode(params)
    try:
        response = urllib.request.urlopen(url, context=ctx)
        data = response.read().decode()
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve data: {e}")
    print('Retrieving', len(data), 'characters')
    try:
        js = json.loads(data)
    except ValueError:
        raise RuntimeError("Error parsing JSON")
    if 'main' not in js or 'weather' not in js:
        raise RuntimeError("No results found")
    
    return {
        "main": js['weather'][0]['main'],
        "description": js['weather'][0]['description'],
        "temp_min": js['main']['temp_min'],
        "temp_max": js['main']['temp_max'],
        "temp": js['main']['temp'],
        "temp_feels": js['main']['feels_like']
    }

def print_weather(info: dict) -> None: #Printing weather data in a readable format
    print('--------------------------------------------------------')
    print(f'Avg Temperature: {info["temp"]} | Feels like: {info["temp_feels"]}')
    print(f'Min Temperature: {info["temp_min"]} | Max Temperature: {info["temp_max"]}')
    print(f'Precipitation: {info["main"]} | Precipitation description: {info["description"]}')
    print('--------------------------------------------------------')

def main():
#For sending request
    while True: 
        question = input('Do you want to enter a city name(1) or precise location(2)? >>> ').strip()

    #Part 1, using Geocode API 
        if question == '1':
            while True:
                city_name = input('Enter city name >>> ').strip().lower().title()
                if city_name == 'Quit':
                    print('You quit')
                    quit()
                elif len(city_name) < 1:
                    print('City name cannot be empty')
                    continue
                params = {
                    'q': city_name,
                    'appid': api_key,
                    'limit': '1',
                    }
                url = geo_url + '?' + urllib.parse.urlencode(params)
                try:
                    response = urllib.request.urlopen(url, context=ctx)
                    data = response.read().decode()
                except:
                    print('Failed to retrieve data')
                    continue
                try:
                    js = json.loads(data)
                except ValueError:
                    print('Error parsing JSON')
                    continue
                if not js:
                    print('No results found for', city_name)
                    continue
                else: 
                    lat = js[0]['lat']
                    lon = js[0]['lon']
                    city = js[0]['name']
                    country = js[0]['country']
                    print('------')
                    print(f'City: {city}, {country} | Latitude: {lat} | Longitude: {lon}')
                    try: 
                        print_weather(get_weather(lat, lon))
                    except RuntimeError as e:
                        print(e)
                        return
                    break

    #Part 2, using only WeatherMap API
        elif question == '2':
            while True:
                lat = input('Enter latitude >>> ').lower().strip()
                if lat == 'quit':
                    print('You quit')
                    quit()
                elif len(lat) < 1:
                    continue
                lon  = input('Enter longitude >>> ').lower().strip()
                if lon == 'quit':
                    print('You quit')
                    quit()
                elif len(lon) < 1:
                    continue
                try:
                    lat_f = float(lat)
                    lon_f = float(lon)
                except ValueError:
                    print('Please enter valid numerical values for latitude and longitude')
                    continue
                print('------')
                print(f'Latitude: {lat_f} | Longitude: {lon_f}')
                try:
                    print_weather(get_weather(lat_f, lon_f))
                except RuntimeError as e:
                    print(e)
                    return
                break

        elif question == 'quit':
            print('Thank you, bye!')
            quit()
            
        else:
            print('---Invalid input, please enter 1,2 or "quit" to exit---')
            continue

    #Rerun part
        rerun = input('Want to go again? (y/n) >>> ').lower().strip()
        if rerun == 'y' or rerun == 'yes':
            continue
        elif rerun == 'n' or rerun == 'no':
            print('Goodbye!')
            quit()
        else :
            print('Invalid input, exiting...')
            quit()
            
if __name__ == '__main__':
    main()
    