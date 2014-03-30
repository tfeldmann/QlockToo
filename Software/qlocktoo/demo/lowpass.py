import itertools


def lowpass(img):
    """
    A simple pure python low pass (antialiasing) filter.
    Applies a gaussian blur on a 2D list of floats.
    """
    width = len(img[0])
    height = len(img)
    # create result image. The corners will not be altered
    result = [x[:] for x in img]

    mask = [1, 4,  1,
            4, 12, 4,
            1, 4,  1]

    for x, y in itertools.product(range(1, width - 1), range(1, height - 1)):
        part = (img[y - 1][x - 1:x + 2] +
                img[y][x - 1:x + 2] +
                img[y + 1][x - 1:x + 2])
        masked = 1.0 / 32 * sum(map(lambda x, y: x * y, part, mask))
        result[y][x] = masked

    return result


def get_line(x1, y1, x2, y2):
    """
    Python implementation for the bresenham algorithm.
    Returns a list of (x, y) tuples.
    """
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points
