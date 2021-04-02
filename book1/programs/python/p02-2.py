# 乱数を生成するにはrandomというライブラリをimportする必要があります
import random
# importしたrandomの中にある、random()という名前の関数を呼び出します
r = random.random()
# rには、「0以上1未満の実数」が代入されます

# elif を使って記述すると次の通り
if r<1/6:
    print('1の目が出た')
elif 1/6<=r and r<2/6:  # Python独自の条件の書き方に注目
    print('2の目が出た')
elif 2/6<=r and r<3/6:
    print('3の目が出た')
elif 3/6<=r<4/6:
    print('4の目が出た')
elif 4/6<=r<5/6:
    print('5の目が出た')
else:
    print('6の目が出た')

# もちろん、次の様に書いても同じ結果になりますね
if r<1/6:
    print('r<1/6なので、出目は1')
elif r<2/6:
    print('r<2/6なので、出目は2')
elif r<3/6:
    print('r<3/6なので、出目は3')
elif r<4/6:
    print('r<4/6なので、出目は4')
elif r<5/6:
    print('r<5/6なので、出目は5')
else:
    print('r<1なので、出目は6')
