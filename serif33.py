#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

os.chdir('/files/directory')

# JpnとEngのリスト作成
with open('TriJpnRaw.md', 'r') as f:
    dataJpn = f.read()
listJpn = dataJpn.split('\n')

with open('TriEngWork.md', 'r') as f:
    dataEng = f.read()
listEng = dataEng.split('\n')

'''
# 確認用pok
print(listJpn)
print(listEng)
'''
'''
# リストから取り出してみたok
num = 3
nump = listJpn[num]
print(nump)
'''

# {{セリフ3|番号|キャラ名（日本語）|キャラ名（英語）|セリフ（日）|セリフ（英）}}


# リスト作る
verseList = []
for i, (lineJpni, lineEngi) in enumerate(zip(listJpn, listEng)):
    iStr = str(i)
    verse = '{{セリフ3' + '|' + iStr + '.' + '|nameJ|nameE|' +  lineJpni + '|' + lineEngi + '}}' + '\n'
    verseList.append(verse)

# 書き込むファイル開く、なければ作られる
f = open('セリフ3.txt', 'w')
for o in verseList:
    f.write(str(o) + '\n')
f.close()
# おわり
