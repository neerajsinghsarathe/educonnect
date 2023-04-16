import requests


def login(email, password, userType):
    url = f"http://localhost:8000/login/{userType}"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.request("POST", url, json=payload)
    return response.json()['status']


def enrollCourse(courseName):
    url = f"http://localhost:8000/enrollCourse/{courseName}"

    response = requests.request("POST", url)
    return response.json()


def submit(data, pageName):
    url = f"http://localhost:8000/submit/{pageName}"

    response = requests.request("POST", url, json=data)
    return response.json()
