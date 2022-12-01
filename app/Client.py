import time
import queue
import random
import requests

from threading import Thread

from app.modules import *
from app.utils.RestaurantsHandler import RestaurantsHandler


class Client(Thread):
    def __init__(self, client_id, *args, **kwargs):
        super(Client, self).__init__(name=f'Client-{client_id}', *args, **kwargs)
        self.client_id = client_id
        self.__private_list = queue.Queue()
    

    # Overide the run() method of the Thread class.
    def run(self):
        # Get the menus from available restaurants.
        menu = RestaurantsHandler.handle_restaurants()

        # Hmmm... 😴💤
        time.sleep(random.randint(5, 10) * TIME_UNIT)

        # Generate order based on the menu.
        order = self.generate_order(menu)

    
        response = requests.post(
            url=f'http://food-ordering:{FOOD_ORDERING_PORT}/order',
            json=order
        )

        # NOTE! the call to get() will block until an item is available to retrieve from the queue.
        _ = self.__private_list.get()

        # TODO: Function to rate the order here.
    

    def generate_order(self, menu):
        # Get the number of available restaurants.
        n = menu.get('restaurants')

        # Select random restaurants' ids from the list.
        restaurants_ids = random.sample(range(1, n + 1), random.randint(1, n))
        
        order_menu = [{
            'restaurant_id': id,
            'items': random.choices(self.__get_restaurant_menu(id, menu), k=random.randint(1, 5)),
            'priority': None,
            'max_wait': None,
            'created_time': time.time()
        } for id in restaurants_ids]

        order = {
            'client_id': self.client_id,
            'orders': order_menu
        }

        return order
    

    def __get_restaurant_menu(self, restaurant_id, menu):
        restaurant_menu = menu.get('restaurants_data')

        r = filter(lambda el: (el.get('id') == restaurant_id), restaurant_menu)
        
        return list(int(x) for x in list(r)[0].get('menu'))
    
