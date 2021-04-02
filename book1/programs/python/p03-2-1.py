# whileを使って1から10までの合計sumを求めます

n = 10
sum = 0
while n>0:
    sum = sum + n
    n = n - 1

print( 'sum=', sum )

# フィボナッチ数列

a, b = 0, 1
print( a, end=", " )
while b < 10:
    a, b = b, a + b
    print( a, end=", " )

print( b )
