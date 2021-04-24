import requests


def send_token(data, username, password):
    """This func post requesting to api and return auth-token"""
    payload = data.datapros(username, password)
    auth_token = requests.post(data.auth_url, json=payload)

    return auth_token.text


def send_profile(data, token):
    """It returns profile information"""
    headers = data.tokenpros(token)
    profile_info = requests.get(data.profile_url, headers=headers)
    return profile_info.text


def send_lessons(data, token):
    """It returns all the lessons"""
    headers = data.tokenpros(token)
    lessons = requests.get(data.lessons_url, headers=headers)
    return lessons.text


def send(data, url, token):
    """It returns profile information"""
    headers = data.tokenpros(token)
    resp = requests.get(url, headers=headers)
    return resp.json()
