# from exceptions import ApiException
from client import Client
import json

class Lexicon(Client):
    """Lexicon class"""

    def __init__(self, language='hr'):
        super(Lexicon, self).__init__()
        self.language = language

    def queryEntries(self, surface=None, lemma=None, msd=None, rhymes_with=None, no_of_syllables=None,
                      surface_is_regex=False, lemma_is_regex=False, msd_is_regex=False):

        if not self._auth.hasToken():
            raise ValueError("Unauthorized")

        if self.language is None:
            raise ValueError("Language not set")

        params = {}
        if surface is not None:
            params['surface'] = surface
        if lemma is not None:
            params['lemma'] = lemma
        if msd is not None:
            params['msd'] = msd
        if rhymes_with is not None:
            params['rhymes_with'] = rhymes_with
        if no_of_syllables is not None:
            params['no_of_syllables'] = no_of_syllables

        if surface_is_regex is not None:
            params['surface_is_regex'] = "1" if surface_is_regex else "0"
        if lemma_is_regex is not None:
            params['lemma_is_regex'] = "1" if lemma_is_regex else "0"
        if msd_is_regex is not None:
            params['msd_is_regex'] = "1" if msd_is_regex else "0"

        # if rhyming_function is not None:
        #     params['rhyming_function'] = marshal.dumps(rhyming_function.func_code)

        return self.queryApi("{0}/lexicon".format(self.language), params)