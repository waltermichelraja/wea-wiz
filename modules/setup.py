import requests
import os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

load_dotenv("config/.env")

class WeaWiz:
    def __init__(self, city) -> None:
        self.city = city
        self.response = None
        self.data = None

    def fetch_api(self):
        ROOTW = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={os.getenv('APIKEY')}&units=metric"
        self.response = requests.get(ROOTW)
        self.data = self.response.json()

    def get_coords(self):
        coord = self.data.get("coord", {})
        return coord.get("lat"), coord.get("lon")

    def get_timestamp(self):
        from datetime import datetime
        import pytz
        tzone = pytz.timezone('Asia/Kolkata')
        ist_current = datetime.now(tzone)
        return ist_current.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_location_suggestions(query):
        geolocator = Nominatim(user_agent="weawiz_app")
        locations = geolocator.geocode(query, exactly_one=False, limit=5)
        if locations:
            return [{"name": loc.address, "country": loc.raw.get("display_name").split(",")[-1].strip()} for loc in locations]
        return []
