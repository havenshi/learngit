def color(real, guess):
    hits = 0
    for i in range(len(real)):
        if real[i] == [i]:
            hits += 1
            real = real[:i] + real[i+1:]
            guess = guess[:i] + guess[i + 1:]
    map1 = {}
    for i in range(len(real)):
        if real[i] not in map1:
            map1[real[i]] = 1
        else:
            map1[real[i]] += 1
    for i in range(len(guess)):
        pseudohits = 0
        if guess[i] in map1 and map1[guess[i]] > 0:
            pseudohits += 1
            map1[guess[i]] -= 1
    return hits, pseudohits