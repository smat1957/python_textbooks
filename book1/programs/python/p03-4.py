list = [9, 7, 11, 5, 6, 3, 4, 9, 5]

# 偶数が含まれているかチェックする
for i in list:
    if i%2==0:
        print( i, '偶数ありました。終わります。\n')
        break;
    else:
        print( i, 'は奇数です')

# 偶数だけを印刷する
for i in list:
    if i%2==1:
        continue
    print( i, 'は偶数です')
