# Information encryption

a="cagy"
b=33

print(''.join([chr((ord(i)-ord('a')+b)%26+ord('a')) for i in a]))
