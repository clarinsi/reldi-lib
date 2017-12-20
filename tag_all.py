#!/usr/bin/python
from reldi.tagger import Tagger
from reldi.lemmatiser import Lemmatiser
from getpass import getpass
import json
import argparse
import os
user='user'
coding='utf8'

def write(result,file):
    final=set()
    for sentence in result['sentences']['sentence']:
        final.add(sentence['tokenIDs'].split(' ')[-1])
    for token,lemma,tag in zip(result['tokens']['token'],result['lemmas']['lemma'],result['POStags']['tag']):
        file.write((token['text']+'\t'+lemma['text']+'\t'+tag['text']+'\n').encode(coding))
        if token['ID'] in final:
            file.write('\n')
    file.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Tagger and lemmatiser for Slovene, Croatian and Serbian\nUses the ReLDI API. For access rights visit http://nl.ijs.si/services/.')
    parser.add_argument('lang',help='language of the text(s)',choices=['sl','hr','sr'])
    parser.add_argument('path',help='Path to the file or folder containing files (with .txt extension) to be tagged and lemmatised.')
    args=parser.parse_args()
    passwd=getpass('Input password for user "'+user+'": ')
    tagger = Tagger(args.lang)
    tagger.authorize(user, passwd)
    if os.path.isfile(args.path):
        write(json.loads(tagger.tagLemmatise(open(args.path).read().decode(coding).encode('utf8'))),open(args.path+'.taglem','w'))
    else:
        files=[e for e in os.listdir(args.path) if e.endswith('.txt')]
        for index,file in enumerate(files):
            print 'Processing',index+1,'/',len(files)
            write(json.loads(tagger.tagLemmatise(open(os.path.join(args.path,file)).read().decode(coding).encode('utf8'))),open(os.path.join(args.path,file)+'.taglem','w'))
