import requests
import pandas as pd
from datetime import datetime
import os

def get_user_location():
    """
    Automatically retrieves the user’s geographical location
    via the ip-api.com API (free, no key required).
    """
    geo_url = "http://ip-api.com/json/"
    response = requests.get(geo_url).json()

    return {
        "lat": response["lat"],
        "lon": response["lon"],
        "city": response["city"],
        "country": response["country"]
    }

def load_data():
    """
    Retrieves real-time weather data based on the user’s location
    and saves it daily to a CSV file.
    """

    # 1. Automatic localisation
    location = get_user_location()
    lat = location["lat"]
    lon = location["lon"]

    print(f"Location detected : {location['city']} ({location['country']})")
    print(f"Latitude: {lat}, Longitude: {lon}")

    # 2. Weather API call using the detected coordinates
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    response = requests.get(weather_url)
    data = response.json()["current_weather"]

    # 3. Conversion to a DataFrame
    df = pd.DataFrame([{
        "timestamp": datetime.utcnow().isoformat(),
        "city": location["city"],
        "country": location["country"],
        "temperature": data["temperature"],
        "windspeed": data["windspeed"],
        "weathercode": data["weathercode"]
    }])

    # 4. Daily storage
    filename = "weather_history.csv"

    if os.path.exists(filename):
        df.to_csv(filename, mode="a", header=False, index=False)
    else:
        df.to_csv(filename, index=False)

    print(f"Weather data stored in {filename}")
    return df
