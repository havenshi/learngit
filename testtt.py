#Print the RMB amount
#coding:utf-8
a=-27050300
bigFormat={0:u'零',1:u"壹",2:u"贰",3:u'叁',4:u'肆',5:u'伍',6:u'陆',7:u'柒',8:u'捌',9:u'玖'}
unit =['',u'拾',u'佰',u'仟',u'万']

rmb=""

for i, v in enumerate(str(abs(a))):
    rmb+=bigFormat[int(v)]+unit[(len(str(abs(a)))-1-int(i))%4]

    if int(len(str(abs(a)))-i)==5:
        rmb+=unit[4]

rmb+=u'圆'

rmb = rmb.replace(u'零仟', u'零')
rmb = rmb.replace(u'零佰', u'零')
rmb = rmb.replace(u'零拾', u'零')
rmb = rmb.replace(u'零圆', u'圆')

for i in range(len(rmb)-1,0,-1):
  if rmb[i]== rmb[i-1]:
     rmb=rmb[:i]+rmb[i+1:]

rmb = rmb.replace(u'零万', u'万')
rmb = rmb.replace(u'零圆', u'圆')

if a!=abs(a):
    rmb=u'负'+rmb

print rmb