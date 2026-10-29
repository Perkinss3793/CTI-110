# Skyy Perkins
# 10/29/2026
# Used AI to create a Python program

import json
import urllib.request

# 1. Define location parameters for Kannapolis, NC
latitude = 35.4874
longitude = -80.6217
timezone = "America/New_York"

# 2. Build the Open-Meteo API URL requesting current weather and daily highs/lows
# - temperature_unit=fahrenheit ensures all temperatures are returned in °F
# - wind_speed_unit=mph ensures wind speed is returned in mph
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code"
    f"&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset"
    f"&temperature_unit=fahrenheit"
    f"&wind_speed_unit=mph"
    f"&timezone={timezone}"
)

# A simple dictionary mapping WMO Weather Codes to human-readable text descriptions
WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Slight Snowfall",
    73: "Moderate Snowfall",
    75: "Heavy Snowfall",
    80: "Slight Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
}

try:
    # 3. Fetch data from the API endpoint
    req = urllib.request.Request(url, headers={"User-Agent": "Python-Weather-App"})
    with urllib.request.urlopen(req) as response:
        # Parse the JSON response into a Python dictionary
        data = json.loads(response.read().decode())

    # 4. Extract data sections
    current = data["current"]
    daily = data["daily"]
    weather_desc = WEATHER_CODES.get(current["weather_code"], "Unknown")

    # 5. Format and display the output neatly
    print("=" * 45)
    print("      CURRENT WEATHER: KANNAPOLIS, NC      ")
    print("=" * 45)
    print(f"  Timezone           : {data['timezone']}")
    print(f"  Observation Time   : {current['time'].replace('T', ' ')}")
    print(f"  Condition          : {weather_desc}")
    print("-" * 45)
    print(f"  Current Temp       : {current['temperature_2m']} °F")
    print(f"  Feels Like         : {current['apparent_temperature']} °F")
    print(f"  Humidity           : {current['relative_humidity_2m']}%")
    print(f"  Wind Speed         : {current['wind_speed_10m']} mph")
    print("-" * 45)
    print(f"  Today's High       : {daily['temperature_2m_max'][0]} °F")
    print(f"  Today's Low        : {daily['temperature_2m_min'][0]} °F")
    print(
        f"  Sunrise            : {daily['sunrise'][0].split('T')[1]} AM (Local)"
    )
    print(f"  Sunset             : {daily['sunset'][0].split('T')[1]} PM (Local)")
    print("=" * 45)

except Exception as e:
    print(f"An error occurred while fetching the weather: {e}")