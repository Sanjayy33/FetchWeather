from django.shortcuts import render
from django.conf import settings
import requests 

def get_weather(req):
    context = {}
    city = req.GET.get("city")

    if city:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q":city,
            "appid":settings.WEATHER_API_KEY,
            "units":"metric"
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            context["weather"] = {
                "city":data["name"],
                "temp":data["main"]["temp"],
                "description":data["weather"][0]["description"],
            }
        except  requests.exceptions.RequestException:
            context["error"] = "Could not fetch Weather data. Tey again"

    return render(req, "weather.html", context)