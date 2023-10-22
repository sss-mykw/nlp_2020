# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

from operator import add
from functools import reduce
from itertools import zip_longest

input_text1 = 'パトカー'
input_text2 = 'タクシー'

"""
mapでリストを作成し、文字列連結をする
"""

# パターン１
# cross_list = list(map(add, input_text1, input_text2))
# output_text = reduce(add, cross_list)

# パターン２
# cross_list = [None] * (len(input_text1) + len(input_text2))
# cross_list[::2] = input_text1
# cross_list[1::2] = input_text2
# output_text = reduce(add, cross_list)

# パターン３
output_text = []
# zip_longestはzipと違って、引数のリスト同士の要素数が異なる場合に足りない要素を任意の値で埋めることが出来る
for input1, input2 in zip_longest(input_text1, input_text2, fillvalue=''):
    output_text.extend([input1, input2])

print(reduce(add, output_text))
