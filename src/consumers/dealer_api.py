import requests
import os

base_url = os.getenv('BASE_URL')
url = f'{base_url}/join-game'


def dealer_login(user_id: str, username: str, public_api_url: str):
    response = requests.post(url, json={
        'id': user_id,
        'name': username,
        'publicApiUrl': public_api_url
    })
    return response.status_code
