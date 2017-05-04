def answer(total_lambs):
    # your code here
    gen = 1
    while pow(2, gen) - 1 <= total_lambs:
        gen += 1
    gen -= 1

    map = {1: 1, 2: 1}
    result = 2
    if total_lambs == 1:
        return 1
    if total_lambs == 2:
        return 2
    sti = 2
    while result <= total_lambs:
        sti += 1
        map[sti] = map[sti - 1] + map[sti - 2]
        result += map[sti]
    sti -= 1

    return sti - gen
print answer(143)