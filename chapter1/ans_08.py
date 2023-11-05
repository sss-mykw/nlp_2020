"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def ciper_algorithm(character: str) -> str:
    return chr(219 - ord(character)) if character.islower() else character


def cipher(input_text: str) -> str:
    return ''.join(map(ciper_algorithm, input_text))


original_input_text = "The customer that I cook for enjoy this dish every year."
print("暗号化を行う文章：{}".format(original_input_text))

encryption_text = cipher(original_input_text)
print("暗号化　　　　　：{}".format(encryption_text))

decryption_text = cipher(encryption_text)
print("復号化　　　　　：{}".format(decryption_text))
