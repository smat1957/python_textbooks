# 絶対値を求めます
s = input('整数を入力：')
# 入力された文字列 s を整数 n に変換します
n = int( s )

# 正の数或いは0だったら、何もしません(そのままpass)
# 負の数だったら、−１をかけて正の数にします
if n<0:
    n = -n
# 求めた絶対値を出力します
print('絶対値は', n)

# その値は偶数か奇数かを判定します
if n%2==0:
    print( str(n) + 'は偶数です')
else:
    print( str(n) + 'は奇数です')

