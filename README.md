# Python Location Lookup

A small terminal project I made about one month after I started learning Python.

The first version looked up a place and printed location information. I later changed it to check current weather by city name or latitude and longitude. This project is part of my learning journey with Python.

## What it does

- Lets you enter a city name or coordinates.
- Finds city coordinates using OpenWeatherMap’s geocoding API.
- Shows temperature, feels-like temperature, minimum and maximum temperature, and weather conditions.
- Uses Celsius for temperatures.
- Lets you repeat the lookup or quit.

## What I practiced

- User input, loops, and conditions
- Writing and using functions
- Working with dictionaries and JSON
- Making HTTP requests with `urllib`
- Reading an API key from an environment variable
- Basic error handling

## Requirements

- Python 3
- An internet connection
- An [OpenWeatherMap API key](https://home.openweathermap.org/users/sign_up) with access to current weather and geocoding

The script uses Python’s standard library, so there are no extra packages to install.

## How to run

Clone the repository:

```sh
git clone https://github.com/ninplu/python-location-lookup.git
cd python-location-lookup
```

Set your API key and run the script in the same terminal.

### macOS / Linux

```sh
export WEATHER_API_KEY="your_api_key_here"
python3 weather_lookup.py
```

### Windows PowerShell

```powershell
$env:WEATHER_API_KEY = "your_api_key_here"
python weather_lookup.py
```

Replace `your_api_key_here` with your own API key. Keep it out of the source code and GitHub.

The script reads the environment variable directly. It does not automatically load a `.env` file.

## Using the script

Choose:

- `1` to enter a city, such as `Vienna,AT`
- `2` to enter latitude and longitude, such as `48.2082` and `16.3738`
- `quit` to exit

You can also type `quit` at the city or coordinate prompts. After a lookup, enter `y` to try again or `n` to exit.

## Project structure

```text
python-location-lookup/
├── weather_lookup.py
├── README.md
└── .gitignore
```

## Limitations

This is an early learning project with basic error handling.

- City lookup uses the first matching result. Adding a country code can help when several places share a name.
- The script shows current weather, not a forecast.
- Minimum and maximum temperatures come from the current-weather response; they are not the predicted daily low and high.
- Requests depend on your internet connection and OpenWeatherMap API access.

## Project history

The original `Geo-look.py` used the [PY4E OpenGeo service](https://py4e-data.dr-chuck.net/opengeo) to display location details, including coordinates, timezone, and plus code.

The newer version uses [OpenWeatherMap](https://openweathermap.org/) to find city coordinates and retrieve weather. It replaces the old location-detail output.

I have kept the project simple, with small cleanup changes to make it easier to read and run.
