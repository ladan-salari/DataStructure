from sys import stdin
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    start_points = []
    end_points =[]
    lines = []
    for s in segments:
        start_points.append(s.start)
        end_points.append(s.end)
    for i in range(len(segments)):
        tu = (start_points[i], end_points[i])
        lines.append(tu)

    lines_sorted = sorted(lines, key=itemgetter(1))
    points = []
    i = 0

    while i < n:
        seg = lines_sorted[i][1]
        points.append(seg)
        p = i + 1

        if p >= n:
            break
        arrived = lines_sorted[p][0]
        while seg >= arrived:
            p += 1
            if p >= n:
                break
            arrived = lines_sorted[p][0]
        i = p

    return points



if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # optimal_points(segments)

    points = optimal_points(segments)
    print(len(points))
    print(*points)