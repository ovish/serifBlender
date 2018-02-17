#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

os.chdir('/path/to/files/directory')

# JpnとEngのリスト作成
# 1行目は、タイトルなどの、セリフ内容と関係のないものであること
with open('TriJpnFixNR.md', 'r') as f:
    listJpn = f.read().split('\n')
with open('TriEngWorkSasJ.md', 'r') as f:
    listEng = f.read().split('\n')

with open('wordPerTime.txt', 'r') as f:
    listTime = f.read().split('\n')
    listTime.insert(0, 'padding') #0行合わせ

# {{セリフ3|番号|キャラ名（日本語）|キャラ名（英語）|セリフ（日）|セリフ（英）}}
# リスト作る
verseList = [
    '{{セリフ4' + '|' + str(i) + '.' + '|nameJ|nameE|' +  lineJpni + '|' + lineEngi + '|' + str(lineTime) + '|' + '}}'
    for i, (lineJpni, lineEngi, lineTime) in enumerate(zip(listJpn, listEng, listTime))
    ]

with open('セリフ4.txt', 'w') as f:
        f.write('\n'.join(verseList))
# おわり
