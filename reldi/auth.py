from connection import Connection
import json


class Auth(object):
    def __init__(self):
        self._connection = Connection.getInstance()
        self._token = None

    def requestToken(self, username, password):
        url = "/api/v1/login"
        if username is None:
            raise ValueError("Username not specified")

        if password is None:
            raise ValueError("Password not specified")

        params = {
            "username": username,
            "password": password
        }
        response = self._connection.post(url, params)
        if response.status == 200:
            content = response.read().decode('utf-8')
            self._token = json.loads(content)
        else:
            raise ValueError(response.read)

    def getToken(self):
        return self._token

    def hasToken(self):
        return self._token is not None
