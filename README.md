# The ReLDI web services library

This repository contains the documentation and some handy scripts for using the ReLDI web services library.

[ReLDI](https://reldi.spur.uzh.ch) is a SNSF-funded SCOPES project under which a series of resources and tools for processing South-Slavic languages were developed.

Some of the tools available through the library / web services were developed inside the [JANES](http://nl.ijs.si/janes/) and [CLARIN.SI](https://www.clarin.si) projects.

## Installing the library

The easiest way to install the ReLDI library is through [PyPI](https://pypi.python.org/pypi) from your command line interface.

```
$ sudo pip install reldi
```

## Using the library

### Scripts

The easiest way to use the library is through two handy scripts available from this repository.

If you require diacritic restoration, you want to use the ```restore_all.py``` script:

```
$ python restore_all.py hr example.txt
```

You can observe the output of the script in the file ```example.txt.redi```. Notice that batch file processing is available as well. You can get more info by running ```$ python restore_all.py -h```.

If you require tokenisation, morphosyntactic tagging and / or lemmatisation, you will want to use the ```tag_all.py``` script:

```
$ python tag_all.py hr example.txt.redi
```

You can inspect the output of the script in the file ```example.txt.redi.taglem```. The interface of both scripts is very similar.

### Library

If you want to use the web service responses in your own code, you probably want to use the library directly. Below we are giving simple examples of the diacritic restorer and the tokeniser / tagger / lemmatiser from the Python interactive mode:

```
>>> from reldi.restorer import DiacriticRestorer
>>> dr=DiacriticRestorer('hr')
>>> dr.authorize('my_username','my_password')
>>> eval(dr.restore('Cudil bi se da ovo dela.'))  
{'orthography': [{'tokenIDs': 't_0', 'ID': 'pt_0', 'value': '\xc4\x8cudil'}, {'tokenIDs': 't_1', 'ID': 'pt_1', 'value': 'bi'}, {'tokenIDs': 't_2', 'ID': 'pt_2', 'value': 'se'}, {'tokenIDs': 't_3', 'ID': 'pt_3', 'value': 'da'}, {'tokenIDs': 't_4', 'ID': 'pt_4', 'value': 'ovo'}, {'tokenIDs': 't_5', 'ID': 'pt_5', 'value': 'dela'}, {'tokenIDs': 't_6', 'ID': 'pt_6', 'value': '.'}], 'text': 'Cudil bi se da ovo dela.', 'tokens': [{'endChar': '5', 'startChar': '1', 'ID': 't_0', 'value': 'Cudil'}, {'endChar': '8', 'startChar': '7', 'ID': 't_1', 'value': 'bi'}, {'endChar': '11', 'startChar': '10', 'ID': 't_2', 'value': 'se'}, {'endChar': '14', 'startChar': '13', 'ID': 't_3', 'value': 'da'}, {'endChar': '18', 'startChar': '16', 'ID': 't_4', 'value': 'ovo'}, {'endChar': '23', 'startChar': '20', 'ID': 't_5', 'value': 'dela'}, {'endChar': '24', 'startChar': '24', 'ID': 't_6', 'value': '.'}], 'sentences': [{'tokenIDs': 't_0 t_1 t_2 t_3 t_4 t_5 t_6', 'ID': 's_0'}]}

>>> from reldi.tagger import Tagger
>>> t=Tagger('hr')
>>> t.authorize('my_username','my_password')
>>> eval(t.tagLemmatise(u'Ovi alati rade dobro.'.encode('utf8')))
{'tokens': [{'endChar': '3', 'startChar': '1', 'ID': 't_0', 'value': 'Ovi'}, {'endChar': '9', 'startChar': '5', 'ID': 't_1', 'value': 'alati'}, {'endChar': '14', 'startChar': '11', 'ID': 't_2', 'value': 'rade'}, {'endChar': '20', 'startChar': '16', 'ID': 't_3', 'value': 'dobro'}, {'endChar': '21', 'startChar': '21', 'ID': 't_4', 'value': '.'}], 'lemmas': [{'tokenIDs': 't_0', 'ID': 'le_0', 'value': 'ovaj'}, {'tokenIDs': 't_1', 'ID': 'le_1', 'value': 'alat'}, {'tokenIDs': 't_2', 'ID': 'le_2', 'value': 'raditi'}, {'tokenIDs': 't_3', 'ID': 'le_3', 'value': 'dobro'}, {'tokenIDs': 't_4', 'ID': 'le_4', 'value': '.'}], 'text': 'Ovi alati rade dobro.', 'POSTags': [{'tokenIDs': 't_0', 'ID': 'pt_0', 'value': 'Pd-mpn'}, {'tokenIDs': 't_1', 'ID': 'pt_1', 'value': 'Ncmpn'}, {'tokenIDs': 't_2', 'ID': 'pt_2', 'value': 'Vmr3p'}, {'tokenIDs': 't_3', 'ID': 'pt_3', 'value': 'Rgp'}, {'tokenIDs': 't_4', 'ID': 'pt_4', 'value': 'Z'}], 'sentences': [{'tokenIDs': 't_0 t_1 t_2 t_3 t_4', 'ID': 's_0'}]}

```
