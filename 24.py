# take the lead
m=2
n=1

if m < n:
    m, n = n, m

horse = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-2,-1),(-1,-2),(1, -2), (2, -1)]
queue = [(0, 0)]
goal = {(0, 0): 0}

while queue != []:
    base = queue.pop(0)

    for item in horse:
        arrow = ((item[0] + base[0]), (item[1] + base[1]))
        if 0 <= arrow[0] <= m and 0 <= arrow[1] <= n and (not arrow in goal):
            goal[arrow] = goal[base] + 1  # how many steps
            queue.append(arrow)
            if arrow == (m, n):
                break

if (m, n) in goal:
    print goal[(m, n)]
else:
    print -1
print goal