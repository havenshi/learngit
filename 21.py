# Back to the text string

a="xabcbai"
n=5
print('YES' if [i for i in range(len(a)-n+1) if a[i:(i+n)] == a[i:(i+n)][::-1]] else 'NO')