import random

# 実は、こうするとサイコロは簡単に実現できる
# 1 以上 6 以下
n = random.randint(1, 6)
print('出目は、', n )

# これでもいい
# 0 以上 1 未満
r = random.random()
n = int( r*6 + 1 )
print('出目は、', n )

# 或いは
# 0 以上 6 未満
r = random.uniform(0, 6)
n = int(r + 1)
print('出目は、', n )

# これの方が簡単
# 1 以上 7 未満
r = random.uniform(1, 7)
n = int( r )
print('出目は、', n )

