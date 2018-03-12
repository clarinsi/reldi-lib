# from exceptions import ApiException
from client import Client
import json

class NERTagger(Client):
    """Lexicon class"""

    def __init__(self, language='hr'):
        super(NERTagger, self).__init__()
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

        return self.queryApi("{0}/tag_lemmatise_ner".format(self.language), params)
