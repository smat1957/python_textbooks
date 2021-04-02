# 文字列はクォーテーション・マークで挟む
msg = 'Hello'
print( msg )

# 文字列は配列に入っている
# インデックスは０から始まる
print( msg[0] )

# インデックスに１を指定すると、
# ２文字目が取り出される
print( msg[1] )
print( msg[2] )
print( msg[3] )
print( msg[4] )
print()

# 負のインデックスは、後ろから数える
print( msg[-1] )
print( msg[-2] )
print( msg[-3] )
print( msg[-4] )
print( msg[-5] )

# ６番目の文字は無いのでエラーになる
# IndexError: string index out of range
print( msg[5] )
