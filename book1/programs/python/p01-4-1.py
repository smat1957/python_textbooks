# 大文字小文字の変換
msg = 'HELLO python'
print( msg )
str0 = msg.upper()
print( str0 )
str0 = msg.lower()
print( str0 )
str0 = msg.title()
print( str0 )

# 文字列の置換
str0 = msg.replace( 'HELLO', 'Hi')
print( msg, str0, sep=' --> ' )

# 文字列を空白文字で分割
str0 = '   spam  ham    eggs  '
lst = str0.split()
print( lst )

# 左右の空白文字を削除
str1 = str0.strip()
print( "'" + str1 + "'" )

# 文字列の末尾をチェック
str0 = 'sample.jpg'
bool_result = str0.endswith( ('jpg', 'gif', 'png') )
print( bool_result )

# 文字列が数値の文字列かどうかチェック
str0 = '1234567890'
str1 = 'A234B789C'
bool_result0 = str0.isdigit()
bool_result1 = str1.isdigit()
print( bool_result0 )
print( bool_result1 )

# 文字列の長さを取得
print( len(str0), len(str1) )

# 文字列の中に任意の文字列が存在するかどうかチェック
str0 = 'HELLO python'
bool_result = 'py' in str0
print( bool_result )
bool_result = 'java' in str0
print( bool_result )

# 複数の文字列の連結
str0 = '-'.join( ['spam', 'ham', 'eggs'] )
print( str0 )

# formatメソッド
lang, num, name = 'python', 10, 'taro'
str0 = '{}は{}が好きです'.format(name, lang)
print( str0 )

# 引数の順番で指定
str0 = '{1}は{0}が好きです'.format(lang, name)

# キーワード引数で指定
str0 = '{n}はC言語よりも{num}倍{l}が好きです'.format(l=lang, n=name, num=num)
print( str0 )
