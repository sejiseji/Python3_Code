'''
入力のx値,y値の掛け算表を表示する(表示桁数：最大桁数に調整)
'''
#各計算値を受付
print('x*y の掛け算表を作ります。')
print('x = ?')
xline = int(input())
print('y = ?')
yline = int(input())
#取り得る最大の桁数
keta_max = len(str(xline*yline))
#xカウントアップ中は改行せず、最大桁数に調整して印字。yカウントアップ時に改行
for y in range(1,yline+1):
    for x in range(1,xline+1):
        print(str(x*y).rjust(keta_max+1), end = '')
    print('')
