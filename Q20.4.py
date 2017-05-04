# abcde的c位出现2：
# 如果这位比2小，xx200-xx299都满足条件，xx为1到ab-1
# 如果这位比2大，xx200-xx299都满足条件，xx为1到ab
# 如果这位为2，1到ab-1个xx200-xx299，在加上de+1
def find2(n):
    result = 0
    low, high = 0, 0 # 第i位的后半段和前半段
    factor = 1
    while n/factor > 0:
        low = n - (n/factor) * factor
        cur = n/factor % 10
        high = n/(factor * 10)
        if cur < 2:
            result += high * factor
        elif cur < 2:
            result += (high + 1) * factor
        else:
            result += high * factor + low + 1
        factor *= 10
    return result


