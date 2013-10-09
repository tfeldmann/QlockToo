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

    mask = [1, 2, 1,
            2, 4, 2,
            1, 2, 1]

    for x, y in itertools.product(range(1, width - 1), range(1, height - 1)):
        part = (img[y - 1][x - 1:x + 2] +
                img[y][x - 1:x + 2] +
                img[y + 1][x - 1:x + 2])
        masked = 1.0 / 16 * sum(map(lambda x, y: x * y, part, mask))
        result[y][x] = masked

    return result
