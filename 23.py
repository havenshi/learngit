# 365 Or 366
year="2013"
print(366 if int(year)%400==0 or int(year)%4==0 and int(year)%100!=0 else 365)