# from exceptions import ApiException
from client import Client
import json

class DiacriticRestorer(Client):
    """Lexicon class"""

    def __init__(self, language='hr'):
        super(DiacriticRestorer, self).__init__()
        self.language = language

    def restore(self, text, format='json'):

        if not self._auth.hasToken():
            raise ValueError("Unauthorized")

        if self.language is None:
            raise ValueError("Language not set")

        if text is None:
            raise ValueError("Please specify the input text")

        params = {
            'text': text,
            'format': format
        }

        return self.queryApi("/api/v1/{0}/restore".format(self.language), params)
