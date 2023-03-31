# API
#
# Enables users to interact with the service through HTTP requests
#
# Authors: Lahcène Belhadi <lahcene.belhadi@alumni.univ-avignon.fr>

from flask import Flask

api = Flask(__name__)

@api.get("/")
def root() -> str:
    return "Hello world!"

