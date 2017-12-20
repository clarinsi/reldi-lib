#!/usr/bin/python
from reldi.parser import Parser
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
    sent_offset=0
    token_num=0
    parses=[]
    for tree in result['depparsing']['parse']:
        parses.extend(tree['dependency'])
    for token,lemma,tag,parse in zip(result['tokens']['token'],result['lemmas']['lemma'],result['POStags']['tag'],parses):
        if 'govIDs' not in parse:
            head='0'
        else:
            head=int(parse['govIDs'].split('_')[-1])+1-sent_offset
        file.write((token['text']+'\t'+lemma['text']+'\t'+tag['text']+'\t'+str(head)+':'+parse['func']+'\n').encode(coding))
        token_num+=1
        if token['ID'] in final:
            file.write('\n')
            sent_offset+=token_num
            token_num=0
    file.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Tagger, lemmatiser and parser for Slovene, Croatian and Serbian\nUses the ReLDI API. For access rights visit http://nl.ijs.si/services/.')
    parser.add_argument('lang',help='language of the text(s)',choices=['sl','hr','sr'])
    parser.add_argument('path',help='Path to the file or folder containing files (with .txt extension) to be tagged, lemmatised and parsed.')
    args=parser.parse_args()
    passwd=getpass('Input password for user "'+user+'": ')
    parser=Parser(args.lang)
    parser.authorize(user, passwd)
    if os.path.isfile(args.path):
        write(json.loads(parser.tagLemmatiseParse(open(args.path).read().decode(coding).encode('utf8'))),open(args.path+'.parse','w'))
    else:
        files=[e for e in os.listdir(args.path) if e.endswith('.txt')]
        for index,file in enumerate(files):
            print 'Processing',index+1,'/',len(files)
            write(json.loads(parser.tagLemmatiseParse(open(os.path.join(args.path,file)).read().decode(coding).encode('utf8'))),open(os.path.join(args.path,file)+'.parse','w'))
