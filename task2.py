def task(x1, y1, x2, y2, x3, y3, x4, y4):
    xA = [x1, x2]
    xB = [x3, x4]
    yA = [y1, y2]
    yB = [y3, y4]

    if max(xA) >= min(xB) and min(xA) <= min(xB):
        dx = max(xA) - min(xB)
        dy = 0
        if max(yA) >= min(yB) and min(yA) <= min(yB):
            dy = max(yA) - min(yB)
        return dx * dy
    elif max(xB) >= min(xA) and min(xB) <= min(xA):
        dx = max(xB) - min(xA)
        dy = 0
        if max(yB) >= min(yA) and min(yB) <= min(yA):
            dy = max(yB) - min(yA)
        return dx * dy
    return False


if __name__ == '__main__':
    print(task(1, 1, 2, 2, 3, 3, 4, 4))
    print(task(-5, 2, 3, -2, 2, 6, 5, 1))
    print(task(1, 4, 6, 1, 5, 5, 7, 3))
    print(task(5, 5, 7, 3, 1, 4, 6, 1))
    print(task(-2, 3, 0, -2, 0, -2, 2, -4))
    print(task(2, 5, 6, 1, 3, 4, 5, 2))
