# Py throw the shot put
a=184
b=16
if a<0:
	a=-a
	flag='-'
else:
	flag=''
res=[]
d={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
while a>0:
	res.append(d[a%b])
	a=a//b

print(flag+''.join(res[::-1]))