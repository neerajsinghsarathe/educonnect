import requests


def login(email, password, userType):
    url = f"http://localhost:8000/login/{userType}"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.request("POST", url, json=payload)
    return response.json()['status']

