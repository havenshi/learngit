def answer(plaintext):
    # your code here
    map = {}
    map['a'] = '100000'
    map['b'] = '110000'
    map['c'] = '100100'
    map['d'] = '100110'
    map['e'] = '100010'
    map['f'] = '110100'
    map['g'] = '110110'
    map['h'] = '110010'
    map['i'] = '010100'
    map['j'] = '010110'
    map['k'] = '101000'
    map['l'] = '111000'
    map['m'] = '101100'
    map['n'] = '101110'
    map['o'] = '101010'
    map['p'] = '111100'
    map['q'] = '111110'
    map['r'] = '111010'
    map['s'] = '011100'
    map['t'] = '011110'
    map['u'] = '101001'
    map['v'] = '111001'
    map['w'] = '010111'
    map['x'] = '101101'
    map['y'] = '101111'
    map['z'] = '101011'
    map[' '] = '000000'
    flag = '000001'
    result = ''
    for item in plaintext:
        if item not in map:
            result += flag + map[(item.lower())]
        else:
            result += map[item]
    return result

print answer('The quick brown fox jumped over the lazy dog')