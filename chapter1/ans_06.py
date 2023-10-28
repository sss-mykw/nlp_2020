"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
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


X = set(create_n_gram('paraparaparadise', 2))
print('X:{}'.format(X))
Y = set(create_n_gram('paragraph', 2))
print('Y:{}'.format(Y))

print()

union = X.union(Y)
print('和集合：{}'.format(union))

intersection = X.intersection(Y)
print('積集合：{}'.format(intersection))

symmetric_difference = X.symmetric_difference(Y)
print('差集合：{}'.format(symmetric_difference))
# print('和集合の数 = 積集合 + 差集合')
# print('{0} = {1} + {2}'.format(len(union), len(intersection), len(symmetric_difference)))
# print(union == intersection.union(symmetric_difference))

print()

print("集合Xに'se'が含まれるかどうか：{}".format('se' in X))
print("集合Yに'se'が含まれるかどうか：{}".format('se' in Y))
