"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


def create_n_gram(input_text, n):
    if not (isinstance(input_text, str) or isinstance(input_text, list)):
        return

    if len(input_text) < n:
        return input_text

    n_gram_list = list()
    for index in range(0, len(input_text) - n + 1):
        n_gram_list.append(input_text[index:index + n])

    return n_gram_list


input_text = 'I am an NLPer'
print('単語bi-gram: {}'.format(create_n_gram(input_text.split(), 2)))
print('文字bi-gram: {}'.format(create_n_gram(input_text, 2)))
