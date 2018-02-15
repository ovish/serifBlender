#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

os.chdir('/files/directory')

# JpnとEngのリスト作成
with open('TriJpnFixNR.md', 'r') as f:
    dataJpn = f.read()
listJpn = dataJpn.split('\n')

with open('TriEngWorkSasJ.md', 'r') as f:
    dataEng = f.read()
listEng = dataEng.split('\n')

with open('wordPerTime.txt', 'r') as f:
    listTime = f.read().split('\n')
listTime.insert(0, 'padding') #0行合わせ

# {{セリフ3|番号|キャラ名（日本語）|キャラ名（英語）|セリフ（日）|セリフ（英）}}

# 書き込むファイル開く、なければ作られる
f = open('セリフ4.txt', 'w')
# 整形しつつ書き込む
for i, (lineJpni, lineEngi, lineTime) in enumerate(zip(listJpn, listEng, listTime)):
    iStr = str(i)
    verse = '{{セリフ4' + '|' + iStr + '.' + '|nameJ|nameE|' +  lineJpni + '|' + lineEngi + '|' + str(lineTime) + '|' + '}}' + '\n'
    f.write(verse)
f.close()
# おわり
