class Data:
    """Serialize data"""
    def __init__(self):
        self.auth_url = 'https://yaraapi.mazust.ac.ir/api/auth'
        self.profile_url = 'https://yaraapi.mazust.ac.ir/api/students'
        self.lessons_url = 'https://yaraapi.mazust.ac.ir/api/lessons/student'

    def datapros(self, username, password):
        username = username
        password = password

        payload = {
            "userTypeID": 1,
            "username": f"{username}",
            "password": f"{password}",
        }

        return payload

    def tokenpros(self, token):
        headers = {
            "x-auth-token": f"{token}"
        }

        return headers
