BASE_URL = 'http://127.0.0.1:8000'
import requests
import json
def create_user(full_name,telegram_id):
    url =f"{BASE_URL}/botuser/"
    requests.post(url,data={'full_name':full_name,'telegram_id':telegram_id})
    return 'Ok'
def change(id,lang):
    url = f"{BASE_URL}/change/{id}/{lang}/"
    requests.get(url)
    return 'Ok'
