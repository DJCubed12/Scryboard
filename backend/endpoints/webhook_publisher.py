import requests
from flask import Flask, Response, current_app, request

from repository import CardRepository

subscribers = []

@current_app.post("/webhook_cardupdate")
def webhook_cardupdate():
    sender = request.origin
    if sender not in subscribers:
        subscribers.append(request.origin)
        return {"msg": f"Success! Registered \"{request.origin}\""}
    else:
        return {"msg": "Already registered!"}


def invoke_cardupdate():
    for sub in subscribers:
        requests.post(f"{sub}/cardupdate")