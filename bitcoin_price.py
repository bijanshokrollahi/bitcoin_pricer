"""
copyright bijan shokrollahi
03.17.2022

"""

import logging
import requests
from flask import Flask
from logging_info import setup_logging

BPI = 'bpi'
USD = 'USD'
RATE = 'rate_float'

app = Flask(__name__)
setup_logging()


@app.route("/price")
def price() -> dict:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    resp = requests.get(url)
    logging.info(f"{resp.status_code} {url}")
    # return resp.json().get(BPI, {}).get(USD, {}).get(RATE, float('-inf'))
    return resp.json()

