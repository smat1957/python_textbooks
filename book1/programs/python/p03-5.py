# for の繰り返しで合計を求めます
list = [9, 7, 11, 5, 6, 3, 4, 9, 5]
sum = 0
for index, item in enumerate(list):
    print( 'index=', index, ':', item )
    sum += item
print( 'sum=', sum, '\n' )

# while の繰り返しで、同じく合計を求めます
length = len( list )
index = 0
sum = 0
while index < length:
    item = list[index]
    print( 'list[',index,']=', item )
    sum += item
    index += 1
print( 'sum=', sum )

# リストから繰り返しの要素を順に取り出します
fact = 1
for i in [5, 4, 3, 2]:
    fact = fact * i
print( 'fact=', fact )
