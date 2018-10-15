#!/usr/bin/python
from reldi.restorer import DiacriticRestorer
from getpass import getpass
import json
import argparse
import os
user='user'
coding='utf8'

def write(result,file):
    final=set()
    text=result['text']
    for token,norm in zip(result['tokens']['token'],result['orthography']['correction']):
        if token['text']!=norm['text']:
            text=text[:int(token['start'])-1]+norm['text']+text[int(token['end']):]
    file.write(text.encode(coding))
    file.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Diacritic restorer for Slovene, Croatian and Serbian\nUses the ReLDI API. For access rights visit http://nl.ijs.si/services/.')
    parser.add_argument('lang',help='language of the text(s)',choices=['sl','hr','sr'])
    parser.add_argument('path',help='Path to the file or folder containing files (with .txt extension) to be tagged and lemmatised.')
    args=parser.parse_args()
    passwd=getpass('Input password for user "'+user+'": ')
    restorer = DiacriticRestorer(args.lang)
    restorer.authorize(user, passwd)
    if os.path.isfile(args.path):
        write(json.loads(restorer.restore(open(args.path).read().decode(coding).encode('utf8'))),open(args.path+'.redi','w'))
    else:
        for file in os.listdir(args.path):
            if file.endswith('.txt'):
                write(json.loads(restorer.restore(open(os.path.join(args.path,file)).read().decode(coding).encode('utf8'))),open(os.path.join(args.path,file)+'.redi','w'))
