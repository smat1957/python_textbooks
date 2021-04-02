a = input('整数を入力してください')
# a は文字列

b = int( a )
# b は数値に変換された値

# 絶対値を求める関数を定義
def my_abs( x ):
    if x < 0:
        x = -x
    return x

c = my_abs( b )
d = my_abs( b ) + my_abs( c )

print( 'b=', b )
print( 'c=', c )
print( 'd=', d )
