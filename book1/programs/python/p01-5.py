# 代入操作について理解を深めましょう
a = 10
b =  3
# aとbを入れ替える前の状態
print( '\na=', a )
print( 'b=', b )

# 入れ替えの操作は次の3ステップ
temp = a
a = b
b = temp

# 入れ替えた後のaとbの状態
print( '\na=', a )
print( 'b=', b )

# Pythonらしい方法(aとbの入れ替え)
a, b = b, a
print( '\na=', a )
print( 'b=', b )

# 一気に代入する
c = 0
a = b = c
print( '\na=', a )
print( 'b=', b )
