def wareki( seireki ):
    if seireki<1989:    # 大正の終わりの年は1926年
        return '昭和' + str( seireki-1926+1 ) + '年'
    elif year<2019:     # 昭和の終わりの年は1989年
        return '平成' + str( seireki-1989+1 ) + '年'
    else:               # 平成の終わりの年は2019年
        return '令和' + str( seireki-2019+1 ) + '年'
    
for year in range(1970, 2021):
    print('西暦', year, 'は、', wareki(year) )
