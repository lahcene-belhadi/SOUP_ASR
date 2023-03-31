# API
#
# Enables users to interact with the service through HTTP requests
#
# Authors: Lahcène Belhadi <lahcene.belhadi@alumni.univ-avignon.fr>

from flask import Flask, request

api = Flask(__name__)

@api.get("/")
def root() -> str:
    """Displays an \"Hello world!\""""
    return "Hello world!"

@api.post("/transcribe")
def transcribe() -> str:
    """Enables user to pass an audio file and get the text from their speech"""
    audio_file = request.files.get("audio_file")

    if audio_file is None:
        return "No file provided!"

    return "Got the file!"

