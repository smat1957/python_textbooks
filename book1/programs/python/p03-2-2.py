# breakとcontinueの使われ方を確認しましょう

n = -10
sum = 0
while True:
    print( '途中経過 n=', n, ' sum=', sum )
    n = n + 1
    if n>10:
        break
    if n<=0:
        continue
    sum = sum + n

print( 'sum=', sum )
