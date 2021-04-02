# str( 整数型変数 ) によって「整数→文字列」の変換ができる
price = 100
msg = 'price is ' + str( price ) + ' yen.'
print( msg )
# msg = 'price is ' + price + 'yen.' はエラーになる

# int( 数値の文字列 ) によって「文字列→整数」の変換ができる
nebiki = '10'
urine = price - int( nebiki )
print( urine )
# urine = price - nebiki はエラーになる

# float( 数値の文字列 )によって、「文字列→実数」の変換ができる
pi = float( '3.14159265' )
r = 10.0
area = pi*r**2
# str( 実数型変数 )によって、「実数→文字列」の変換ができる
print( '円の面積は、'+ str(area) )
print( '円周の長さは、', 2.0*pi*r )
