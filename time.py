#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

os.chdir('/fliles/directory')


with open('timeRaw.srt', 'r') as f:
    data = f.read()


# 秒数だけ抜き出すを正規表現で\d{2}\:\d{2}\,\d{2}
pattern = r'\d{2}\:\d{2}\,\d{2}'
matchList = re.findall(pattern, data)


# 1/100秒単位に整える元は 00:58,89
timeList = []
for time in matchList:
    timeS = str(time)
    pattern = r'[0-9]'
    secList = re.findall(pattern, timeS)

    minSec = int(secList[1]) * 60 * 100
    secOnly = ''
    for i in range(2, 6):   # 2=<i<6
        secOnly += str(secList[i])

    secSum = minSec + int(secOnly)
    timeList.append(secSum)


# シーンあたりの秒数を求めるために引き算
diffList = []
for index, time in enumerate(timeList):
    if index % 2 != 0:
        indexMinus = index - 1
        timeLIndex = timeList[index]
        timeLIndexMinus = timeList[indexMinus]
        diff = int(timeLIndex) - int(timeLIndexMinus)
        diffList.append(diff)


# 6かけてピリオド入れる
diffList6 = list(map(lambda x:x*6/float(100), diffList))

# ファイル書き込み
with open('wordPerTime.txt', 'w') as f:
        f.write('\n'.join(diffList6))

'''
# ぶっこむ
with open('セリフ4fix.txt', 'r') as f:
    serif4List = f.read().split('\n')
dstList = []
for serifLine, diffLine in zip(serif4List, diffList6):
    dst = serifLine.replace('|0|', '|' + str(diffLine) + '|')
    dstList.append(dst)
print(dstList)
'''
