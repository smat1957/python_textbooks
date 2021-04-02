# これを繰り返し処理しようとして次のように書いてみる
sum = 0
for i in range(10):
    print( 'i=', i )
    sum = sum + i
print( 'sum=', sum )

# range( 10 ) は10を含まない　要注意！
# 11までとしてみる。11は含まないけど、10まで加算できる
sum = 0
for i in range(11):
    sum = sum + i
print( sum )

# 0を足す操作は不要なので1から加算を始める
sum = 0
for i in range(1, 11):
    sum = sum + i
print( sum )

# 増分を1ずつ増やす指定(特に指定しなくても、1ずつの増分になっているけど)
sum = 0
for i in range(1, 11, 1):
    sum = sum + i
print( sum )

# 増分を2ずつ、とばして加算すると「奇数の和」になる
sum = 0
for i in range(1, 11, 2):
    print( 'i=', i )
    sum = sum + i
print( 'sum=', sum )

# 「偶数の和」を求めるにはどうしたらいいかな？
