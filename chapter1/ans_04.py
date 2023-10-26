"""
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause.
 Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

input_text = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. '
              'Arthur King Can.')

split_word_list = input_text.split()
# print(split_word_list)

element_symbol_map = dict()
index = 0
for word in split_word_list:
    # pythonにはインクリメント演算子がない・・
    index += 1
    # pythonにはswitch文がないのでSetとinを組み合わせて代用する
    if index in {1, 5, 6, 7, 8, 9, 15, 16, 19}:
        element_symbol_map[index] = word[0]
    else:
        element_symbol_map[index] = word[:2]

print(element_symbol_map)
