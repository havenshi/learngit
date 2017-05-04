def paint(screen, x, y, color):
    if x < 0 or x > len(screen) - 1 or y < 0 or y > len(screen[0]) - 1:
        return
    if screen[x][y] == color:
        return
    screen[x][y] = color
    paint(screen, x - 1, y, color)
    paint(screen, x + 1, y, color)
    paint(screen, x, y - 1, color)
    paint(screen, x, y + 1, color)

# bfs
def paint2(screen, x, y, color):
    if x < 0 or x > len(screen) - 1 or y < 0 or y > len(screen[0]) - 1:
        return
    if screen[x][y] == color:
        return
    queue = [[x, y]]
    while queue:
        item = queue.pop()
        screen[item[0], item[1]] = color
        queue.append([x - 1, y])
        queue.append([x + 1, y])
        queue.append([x, y - 1])
        queue.append([x, y + 1])