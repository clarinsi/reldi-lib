# from exceptions import ApiException
from connection import Connection
from auth import Auth
import json
import uuid;

class Client(object):
    def __init__(self):
        self._username = None
        self._password = None
        self._connection = Connection.getInstance()
        self._auth = Auth()

    def authorize(self, username, password):
        self._username = username
        self._password = password
        self._auth.requestToken(username, password)

    def authorizeFromCache(self):
        self._auth.requestToken(self._username, self._password)

    def queryApi(self, url, params):
        # First try
        params['request-id'] = uuid.uuid4().__str__()
        response = self._connection.get(url, params, self._auth.getToken())
        if response.status is 200:
            data_result = response.read()
            return data_result
        # If unauthorized, retry with cached authorization
        elif response.status == 401:
            self.authorizeFromCache()
            response = self._connection.get(url, params, self._auth.getToken())
            if response.status is 200:
                data_result = response.read()
                return data_result
            else:
                raise ValueError(response.read())
        else:
            raise ValueError(response.read())
