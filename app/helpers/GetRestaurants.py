import requests

from app.modules import *
from app.modules import AGGREGATOR_PORT


class GetRestaurants:
    @staticmethod
    def handle_restaurants():
        content = requests.get(
            url=f'http://restaurant-aggregator:{AGGREGATOR_PORT}/menu'
        ).json()

        return content