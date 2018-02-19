# serifBlender
Rwby_Fandom_Wikiので翻訳作業をする時に役立つプログラムの詰め合わせです。 
翻訳自体は表計算ソフトでやったほうが効率が良さそうですが、
プレーンテキストで書きたい、バージョン管理したい、という時に使えます。  
time.pyは、srtファイルから目標文字数を出力するので、
表計算ソフトで翻訳される場合でも、便利に使えます。

## 実行環境
- Lang: python  
- Version: 3(もし2で動かすと日本語がバイナリで出力されます)  
- Os: 多分どこでも動くはず(macos10.13.3で動作確認)  

## 内訳と使い方
### time.py
srt-->>目標文字数
1. os.chdir('/poth/to/files/directory')を書き換えます
2. 目的のsrtファイルを開けるように'with open('ファイル名.srt', 'r')'を書き換えます
3. python3で実行
4. Time.txtが出力されます

### serif33.py/ serif44.py
英語原文、日本語翻訳文、目標文字数-->>セリフ3/セリフ4
1. 原文のtxtファイル、翻訳されたtxtファイル、time.pyで作られたTime.txtを用意します
2. 原文、翻訳、の二つのファイルで同じ内容が同じ行にあることを確認します
3. 原文、翻訳、それぞれ1行目は本文とは関係ないタイトルなどが書かれていることを確認します。さもないとインデックスがずれます。
4. time.pyと同じく必要な箇所を書き換えます
5. それぞれ実行します
6. それぞれ出力されます

### add.py
srt、更新された日本語翻訳文-->>srt(翻訳文を入れ替えたもの)
1. セリフ4から正規表現使うなりして文章だけのファイルを作る
2. 適宜書き換える
3. 実行すると出力される

## ライセンス
MIT
