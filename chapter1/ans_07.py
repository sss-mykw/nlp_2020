# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．

def create_template(x, y, z):
    return '{0}時の{1}は{2}'.format(x, y, z)


print(create_template(12, '気温', 22.4))
