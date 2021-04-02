# 変数の名前にはアルファベットの小文字を使う
# 変数priceに、値100を代入
price = 100
# 変数priceの内容を印刷
print( price )

# 定数の名前にはアルファベットの大文字を使う
# 定数TAX_RATEを定義(税率8%のつもり)
TAX_RATE = 1.08
# 税込み価格を印刷
xprice = price * TAX_RATE
print( xprice )

# 複合代入演算子:代入＝と同時に行う処理を＝の前に書く
# インクリメント(1を足すこと)を複合代入演算子で書いてみる
price += 1
print( price )
# デクリメント(1を減じること)を複合代入演算子で書いてみる
price -= 1
print( price )

# 四則演算など
a = 10
b =  3

print( '\na=', a )
print( 'b=', b )
print( '\na+b=', a + b )
c = a
c += b
print( 'c=', c )
print( '\na-b=', a - b )
c = a
c -= b
print( 'c=', c )
print( '\na*b=', a * b )
c = a
c *= b
print( 'c=', c )
print( '\na/b=', a / b )
c = a
c /= b
print( 'c=', c )
print( '\na//b=', a // b )
c = a
c //= b
print( 'c=', c )
print( '\na%b=', a % b )
c = a
c %= b
print( 'c=', c )
print( '\na**b=', a ** b )
c = a
c **= b
print( 'c=', c )
