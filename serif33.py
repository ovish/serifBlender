#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

os.chdir('/path/to/files/directory')

# JpnとEngのリスト作成
with open('TriJpnRaw.md', 'r') as f:
    listJpn = f.read().split('\n')
with open('TriEngWork.md', 'r') as f:
    listEng = f.read().split('\n')


# {{セリフ3|番号|キャラ名（日本語）|キャラ名（英語）|セリフ（日）|セリフ（英）}}
# リスト作る
verseList = [
    '{{セリフ3' + '|' + str(i) + '.' + '|nameJ|nameE|' + lineJpn + '|' + lineEng + '}}'
    for i, (lineJpn, lineEng) in enumerate(zip(listJpn, listEng))
    ]

# 書き込むファイル開く、なければ作られる
with open('セリフ3.txt', 'w') as f:
    f.write('\n'.join(verseList))
# おわり
