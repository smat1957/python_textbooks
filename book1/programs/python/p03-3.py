# リスト内包表記で、予めリストを作っておいて
n = 5
list = [i for i in range(n, 1, -1)]
print( 'listは、', list )

# そのリストを使って階乗の計算をすると次の通りです
# i に list の中の要素が、順番に取り出されているのが分かります
fact = 1
for i in list:
    print( 'i=', i )
    fact = fact * i
print( 'fact=', fact )
