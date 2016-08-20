# from exceptions import ApiException
from client import Client
import json

class Tagger(Client):
    """Lexicon class"""

    def __init__(self, language='hr'):
        super(Tagger, self).__init__()
        self.language = language

    def tag(self, text, format='json'):

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

        return self.queryApi("/api/v1/{0}/tag".format(self.language), params)

    def tagLemmatise(self, text, format='json'):

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

        return self.queryApi("/api/v1/{0}/tag_lemmatise".format(self.language), params)
