import urllib2
import json
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """Helps to discover current weather data by city name,
        takes "city_name" as argument"""

    def add_arguments(self, parser):
        parser.add_argument('city_name', type=str,
                            help='argument work better in Latin (ASCII) encoding')

    def handle(self, city_name, **options):
        city = city_name.replace(" ", "%20")  # replace spaces for representation in url
        api_key = "1c73822d0b56a00dec472f069e960a8d"
        url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city, api_key)
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        self.stdout.write(
            """Weather in %s - %s
            min temp: %s F
            max temp: %s F
            average temp: %s F
            wind speed: %s meters per second
            sky: %s
            """
            % (data['name'],
               data['sys']['country'],
               data['main']['temp_min'],
               data['main']['temp_max'],
               data['main']['temp'],
               data['wind']['speed'],
               data['weather'][0]['main']
               )
        )
