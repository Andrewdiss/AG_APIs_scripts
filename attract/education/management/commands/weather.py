import json
import urllib2
from urlparse import urlsplit, parse_qs, urlunsplit
from urllib import urlencode
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Helps to discover current weather data by city name'

    def add_arguments(self, parser):
        parser.add_argument('city_name', type=str,
                            help='arguments should be Latin (ASCII) encoding')

    def handle(self, city_name, **options):
        # replace spaces for representation in url
        city = city_name.replace(" ", "%20")

        def set_query_url():
            scheme, netlock, path, query, fragment = urlsplit(settings.API_URL)
            query_param = parse_qs(query)
            query_param['q'] = city
            query_param['appid'] = settings.API_KEY
            new_query = urlencode(query_param, doseq=True)
            return urlunsplit((scheme, netlock, path,
                               new_query, fragment))

        json_obj = urllib2.urlopen(set_query_url())
        data = json.load(json_obj)
        info = {'city': data['name'],
                'country': data['sys']['country'],
                'tmin': data['main']['temp_min'],
                'tmax': data['main']['temp_max'],
                'tavg': data['main']['temp'],
                'wind_sp': data['wind']['speed'],
                'sky': data['weather'][0]['main']
                }
        self.stdout.write(
            """Weather in %(city)s - %(country)s
            min temp: %(tmin)s F
            max temp: %(tmax)s F
            average temp: %(tavg)s F
            wind speed: %(wind_sp)s meters per second
            sky: %(sky)s
            """ % info
            )
