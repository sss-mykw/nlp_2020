# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

input_text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

"""
まず空白で区切る
その後アルファベットの文字数をカウントする際に正規表現を用いてカンマやピリオドを除外し、アルファベットのみをカウントするようにする
"""

split_word_list = input_text.split()


def count_alphabet(value: str):
    # re.findall()は、マッチするすべての部分を文字列のリストとして返す
    return len(re.findall('[A-Za-z]', value))


word_count_list = list(map(count_alphabet, split_word_list))
print(word_count_list)

