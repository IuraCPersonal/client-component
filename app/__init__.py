from flask import Flask

from app.modules import *
from app.Client import Client
from app.helpers.GetRestaurants import GetRestaurants


# Setup Flask and other dependencies.
app = Flask(__name__)

r = GetRestaurants.handle_restaurants()
restaurants_list.update(r)

for index in range(1, AMOUNT_OF_CLIENTS + 1):
    client = Client(index)
    threads[client.name] = client

for index, thread in enumerate(threads.values()):
    thread.start()