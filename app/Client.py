import time
import random
import requests

from threading import Thread

from app.modules import *


# Extend the Thread class to create Threads for the Tables.
class Client(Thread):
    def __init__(self, client_id, *args, **kwargs):
        super(Client, self).__init__(name=f'Client-{client_id}', *args, **kwargs)
        self.client_id = client_id

    # Overide the run() method of the Thread class.
    def run(self):
        while True:
            order = {
                'client_id': self.client_id,
                'orders': self.generate_orders()
            }

            _ = requests.post(
                url=f'http://restaurant-aggregator:{AGGREGATOR_PORT}/order',
                json=order
            )

            time.sleep(15)

    def __get_restaurant_menu(self, restaurant_id):
        return list(restaurants_list['restaurants_data'][restaurant_id]['menu'].keys())

    def generate_orders(self):
        # Select random restaurants' ids from restaurants_list
        order_restaurants_ids = [0, 1]

        order_menu = [{
            'restaurant_id': el,
            'items': [random.choices(self.__get_restaurant_menu(el), k=random.randint(1, 13))], 
        } for el in order_restaurants_ids]

        return order_menu

    