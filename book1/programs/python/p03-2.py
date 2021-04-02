# 5の階乗を計算してみましょう
# 5! = 5 * 4 * 3 * 2 * 1
n = 5
fact = 1
fact = fact * 5
fact = fact * 4
fact = fact * 3
fact = fact * 2
fact = fact * 1
print( 'fact=', fact )

# これを繰り返し処理で記述してみる
# 最後の6は含まれないので、5までになるはず、、、
fact = 1
for i in range(6):
    fact = fact * i
print( 'fact=', fact )

# おっと！最初にi=0をかけてしまうので、ダメですね
# 1から開始する事を指定しなければなりません
fact = 1
for i in range(1, 6, 1):
    fact = fact * i
print( 'fact=', fact )

# これで一応出来ましたが、
# n=5から1まで、逆に1ずつ減らしていくことを考えます
# 1 をかけるのは無駄な処理ですから、2まででいいと思って
n = 5
fact = 1
for i in range(n, 2, -1):
    fact = fact * i
print( 'fact=', fact )

# としてみたら、終わりの2は含まれていませんでした　要注意！！
# 結局、次の形で2までのかけ算にすることができました
n = 5
fact = 1
for i in range(n, 1, -1):
    print( 'i=', i )
    fact = fact * i
print( 'fact=', fact )
