import requests
from django.core.management import BaseCommand

from shiptrader.models import Starship, Listing
from shiptrader.serializers import StarshipSerializer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        starship_url = 'https://swapi.co/api/starships/'
        records = []
        while starship_url:
            print('Reading a page...')
            req = requests.get(url=starship_url)
            req.raise_for_status()
            json_data = req.json()
            starship_url = json_data['next']  # last page sets this value to None
            records += [*json_data['results']]

        print(f'Fetched {len(records)} records')

        for record in records:
            ship = Starship.objects.all().filter(name=record['name'])
            if ship:
                print(f"Ship {record['name']} already exists")
                continue
            try:
                starship_data = {
                    "name": record['name'],
                    'starship_class': record['starship_class'],
                    'manufacturer': record['manufacturer'],
                    'length': record['length'],
                    'hyperdrive_rating': record['hyperdrive_rating'],
                    'cargo_capacity': record['cargo_capacity'],
                    'crew': record['crew'],
                    'passengers': record['passengers'],
                }
                starship = StarshipSerializer(data=starship_data)

                if not starship.is_valid():
                    for e in starship.errors.keys():
                        del starship_data[e]
                    starship = StarshipSerializer(data=starship_data)
                    if not starship.is_valid():
                        raise ValueError('we tried, but failed again :(')

                ship_obj = starship.save()

                Listing.objects.create(
                    ship_type=ship_obj, price=record['cost_in_credits'])
                print(f'Saved {ship_obj.name}')
            except ValueError as e:
                print(e)
