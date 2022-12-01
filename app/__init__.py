from flask import Flask

from app.modules import *
from app.Client import Client


# Setup Flask and other dependencies.
app = Flask(__name__)


for index in range(1, AMOUNT_OF_CLIENTS + 1):
    client = Client(index)
    threads[client.name] = client

for index, thread in enumerate(threads.values()):
    thread.start()