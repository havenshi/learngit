def exchange(string):
    for i in range(len(string)/2):
        swap(string[i], string[len(string) - 1 - i])
        #string = string[:i] + string[len(string) - 1 - i] + string[i+1:len(string) - 1 - i] + string[i] + string[len(string) - 1 - i + 1:]
    return string

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

print exchange('abcde')