import requests

API_KEY = "YOUR_API_KEY"


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},IN&appid=442808a0a1d7cb7c002af8a107a56463&units=metric"
    )
    
    try:

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:

            return None

        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": data.get("rain", {}).get("1h", 0)
        }

        return weather

    except Exception as e:

        print("Weather API Error:", e)

        return None
        