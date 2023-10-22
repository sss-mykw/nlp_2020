# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

input_text = 'stressed'
"""
文字列はイミュータブルなのでリストのようなreversedメソッドはない
→スライスで逆順にする
"""
input_text_reversed = input_text[::-1]

# reversedを用いてイテレータを作成し、リストに変換してからjoinで文字列結合をすることも可能
# input_text_reversed_list = list(reversed(input_text))
# input_text_reversed = ''.join(input_text_reversed_list)

print(input_text_reversed)