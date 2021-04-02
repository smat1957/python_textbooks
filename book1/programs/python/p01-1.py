# 文字列はクォーテーション・マークで挟む
msg = 'Hello'
print( msg )

# 文字列は、プラスの演算子によって結合できる
msg2 = msg + ' ' + 'World!'
print( msg2 )

# 文字列は、ダブル・クォーテーション・マークで挟んでも良い
msg3 = "Hello " + 'everyone.'
print( msg3 )

# 文字列の長さは、len()関数で得られる
print( '文字列の長さは、', len( msg ) )

# エスケープシーケンス
print('abcd\tefgh\tijkl\tmnop\nqrst\tuvwx\tyz\n')
print('ABCDEFGHIJKLM\nNOPQRSTUVWXYZ\n')
