# 乱数を生成するにはrandomというライブラリをimportする必要があります
import random
# importしたrandomの中にある、random()という名前の関数を呼び出します
r = random.random()
# rには、「0以上1未満の実数」が代入されます
print('乱数が出した値は、',r,'でした')

'''
 このrの値を、サイコロを振ったときの出目に対応づけます
 0以上1/6未満だったら、1の目が出たことにします
 1/6以上で2/6未満だったら、2の目が出たことにします
 2/6以上で3/6未満だったら、3の目が出たことにします
 3/6以上で4/6未満だったら、4の目が出たことにします
 4/6以上で5/6未満だったら、5の目が出たことにします
 5/6以上で6/6=1未満だったら、6の目が出たことにします
'''

# if と else だけでサイコロを記述しようとすると
fstr = '出目は{:2d} ({:.3f} <= {:.3f} < {:.3f})'
if r<1/6:
    print(fstr.format(1, 0, r, 1/6))
else:
    if r<2/6:
        print(fstr.format(2, 1/6, r, 2/6))
    else:
        if r<3/6:
            print(fstr.format(3, 2/6, r, 3/6))
        else:
            if r<4/6:
                print(fstr.format(4, 3/6, r, 4/6))
            else:
                if r<5/6:
                    print(fstr.format(5, 4/6, r, 5/6))
                else:
                    print(fstr.format(6, 5/6, r, 6/6))

