import os


threads = dict()

TIME_UNIT = int(os.getenv('TIME_UNIT'))

FOOD_ORDERING_PORT = os.getenv('FOOD_ORDERING_PORT')
AMOUNT_OF_CLIENTS = int(os.getenv('AMOUNT_OF_CLIENTS'))