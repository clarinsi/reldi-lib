# from exceptions import ApiException
from client import Client
import json
import re


class Parser(Client):
    """Lexicon class"""

    def __init__(self, language='hr'):
        super(Parser, self).__init__()
        self.language = language

    def tagLemmatiseParse(self, text, format='json'):

        if not self._auth.hasToken():
            raise ValueError("Unauthorized")

        if self.language is None:
            raise ValueError("Language not set")

        if text is None:
            raise ValueError("Please specify the input text")

        if format == 'tcf':
            text = re.sub(">\\s*<", "><", text.encode('utf-8'))
            text = re.sub("^\\s*<", "<", text.encode('utf-8'))

        params = {
            'text': text,
            'format': format
        }

        return self.queryApi("{0}/tag_lemmatise_depparse".format(self.language), params)
