# Time is money

st="00:00:00"
et="00:00:10"

print abs(int(st.split(':')[0])*3600 + int(st.split(':')[1])*60 + int(st.split(':')[2])-(int(et.split(':')[0])*3600 + int(et.split(':')[1])*60 + int(et.split(':')[2])))
