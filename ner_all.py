#!/usr/bin/python
from reldi.ner_tagger import NERTagger
from getpass import getpass
import json
import argparse
import os
user='user'
coding='utf8'

def write(result,file):
    final=set()
    tokenID_to_ner={}
    for ner_entity in result['namedEntities']['entity']:
        for tokenID in ner_entity["tokenIDs"].split(" "):
            tokenID_to_ner[tokenID]=ner_entity["value"]
    for sentence in result['sentences']['sentence']:
        final.add(sentence['tokenIDs'].split(' ')[-1])
    for token,lemma,tag, in zip(result['tokens']['token'],result['lemmas']['lemma'],result['POStags']['tag']):
        ner_entity=tokenID_to_ner.get(token["ID"],"O")
        file.write((token['text']+'\t'+lemma['text']+'\t'+tag['text']+'\t'+ner_entity+'\n').encode(coding))
        if token['ID'] in final:
            file.write('\n')
    file.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='NER, Tagger and lemmatiser for Slovene, Croatian and Serbian\nUses the ReLDI API. For access rights visit http://nl.ijs.si/services/.')
    parser.add_argument('lang',help='language of the text(s)',choices=['sl','hr','sr'])
    parser.add_argument('path',help='Path to the file or folder containing files (with .txt extension) to be tagged, annotated with NER and lemmatised.')
    args=parser.parse_args()
    passwd=getpass('Input password for user "'+user+'": ')
    ner_tagger = NERTagger(args.lang)
    ner_tagger.authorize(user, passwd)
    if os.path.isfile(args.path):
        write(json.loads(ner_tagger.tag(open(args.path).read().decode(coding).encode('utf8'))), open(args.path + '.tagNERlem', 'w'))
    else:
        files=[e for e in os.listdir(args.path) if e.endswith('.txt')]
        for index,file in enumerate(files):
            print 'Processing',index+1,'/',len(files)
            write(json.loads(ner_tagger.tag(open(os.path.join(args.path, file)).read().decode(coding).encode('utf8'))), open(os.path.join(args.path, file) + '.tagNERlem', 'w'))
