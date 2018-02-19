#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs


# JpnとEngのリスト作成
with open('final.srt', 'r') as f:
    listFinal = f.read().split('\n')
with open('serif4srt.md', 'r') as f:
    listSerif = f.read().split('\n')


# {{セリフ3|番号|キャラ名（日本語）|キャラ名（英語）|セリフ（日）|セリフ（英）}}
# リスト作る
numlist = [str(line) for i, line in enumerate(listFinal) if i % 4 is 0]
timelist = [str(line) for i, line in enumerate(listFinal) if i % 4 is 1]
emptylist = [str(line) for i, line in enumerate(listFinal) if i % 4 is 3]

LastList = [
    numlist[i] +'\n'+
    timelist[i] +'\n'+
    listSerif[i] +'\n'+
    emptylist[i]
    for i, line in enumerate(numlist)]

# 書き込むファイル開く、なければ作られる
with open('wannasleep.srt', 'w') as f:
    f.write('\n'.join(LastList))
# おわり
