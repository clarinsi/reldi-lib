import httplib, urllib


class Connection:
    # Must be passed into the constructor. Ensures the constructor is private
    _THE_MAGIC_WORD = object()
    _instance = None

    # Private object constructor
    def __init__(self, token):
        self._connection = None
        if token is not self._THE_MAGIC_WORD:
            raise ValueError('This is a private constructor. Plase use ::getInstance()')

        config = self.getServerConfig()
        self._connection = httplib.HTTPConnection(config['url'], config['port'])

    def getServerConfig(self):
        return {
            'url': '193.198.213.31',
            'port': 8080
        }

    @classmethod
    def getInstance(cls):
        if Connection._instance is None:
            Connection._instance = Connection(Connection._THE_MAGIC_WORD)

        return Connection._instance

    def get(self, url, params, token):
        requestUrl = url + "?" + urllib.urlencode(params)
        headers = {"Authorization": token.decode('utf-8')}
        self._connection.request("GET", requestUrl, headers=headers)
        return self._connection.getresponse()

    def post(self, url, params, token=None):
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        if token is not None:
            headers["Authorization"] = token.decode('utf-8')

        self._connection.request("POST", url, urllib.urlencode(params), headers)
        return self._connection.getresponse()
