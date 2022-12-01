import requests

from app.modules import FOOD_ORDERING_PORT


class RestaurantsHandler:

    @staticmethod
    def handle_restaurants():
        content = requests.get(
            url=f'http://food-ordering:{FOOD_ORDERING_PORT}/menu'
        ).json()

        return content
