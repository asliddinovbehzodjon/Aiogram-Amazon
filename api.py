BASE_URL = 'https://behzodbot.pythonanywhere.com'
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
def get_image():
    url = f"{BASE_URL}/image/"
    response = requests.get(url)
    data = json.loads(response.text)
    images = [i['image'] for i in data]
    return images



