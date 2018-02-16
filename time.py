#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs
from decimal import Decimal

os.chdir('/poth/to/files/directory')


with open('timeRaw.srt', 'r') as f:
    data = f.read()

# 秒数だけ抜き出すを正規表現で\d{2}\:\d{2}\,\d{2}
# リストの中にリストが入る[['n','o','p',,,{6}],,,{行数}]
secList = [
    re.findall(r'[0-9]', obj)
    for obj in re.findall(r'\d{2}\:\d{2}\,\d{2}', data)
    ]

# 1秒単位に整える元は 00:58,89
minSecList = [int(Lst[1]) * 60
    for Lst in secList]  # 動画３分までだから[0]取ってこなくていい
secOnlyList = [Decimal(''.join(str(Lst[i]) for i in range(2, 6))) / 100
    for Lst in secList]  # 2=<i<6

timeList = [int(minSec) + Decimal(secOnly)
    for (minSec, secOnly) in zip(minSecList, secOnlyList)]

# シーンあたりの秒数を求めるために引き算
diffList = [Decimal(time) - Decimal(timeList[index - 1])
    for index, time in enumerate(timeList)
    if index % 2  is not 0
    ]

# 6かける
wordPerTime = 6
diffListWord = [diffTime * wordPerTime
    for diffTime in diffList]

# ファイル書き込み
with open('Time.txt', 'w') as f:
    f.write('\n'.join(map(str, diffListWord)))
#fin
