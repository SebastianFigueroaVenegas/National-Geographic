import requests

API_BASE_URL = 'http://localhost:8000/api/'

def get_movies():
    response = requests.get(f'{API_BASE_URL}movies/')
    if response.status_code == 200:
        return response.json()  # Devuelve la lista de películas en formato JSON
    else:
        return []

def get_chat_messages():
    response = requests.get(f'{API_BASE_URL}chat/')
    if response.status_code == 200:
        return response.json()  # Devuelve la lista de mensajes de chat en formato JSON
    else:
        return []
    
    
def create_movie(data,files=None):
    url = f"{API_BASE_URL}movies/"
    headers = {'Content-Type': 'multipart/form-data'}
    try:
        response = requests.post(url, data=data, files=files)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def create_chat_message(message, user_id, is_admin=False):
    payload = {
        'sender': user_id,
        'message': message,
        'is_admin': is_admin
    }
    response = requests.post(f'{API_BASE_URL}chat/', data=payload)
    return response.status_code == 201  # Devuelve True si el mensaje fue creado
