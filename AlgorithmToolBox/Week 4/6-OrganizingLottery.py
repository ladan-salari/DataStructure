from sys import stdin

def points_cover_fast(starts, ends, points):
    assert len(starts) == len(ends)
    counts = [0] * len(points)

    points_list = [(i, 's') for i in starts] + [(i, 'e') for i in ends] + [(p, 'p', i) for i, p in enumerate(points)]
    points_list.sort(key=lambda x: (x[0], -ord(x[1])))

    count = 0
    for index, point in enumerate(points_list):
        if point[1] == 's':
            count += 1
        if point[1] == 'p':
            counts[point[2]] = count
        if point[1] == 'e':
            count -= 1

    return counts


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    output_count = points_cover_fast(input_starts, input_ends, input_points)

    print(*output_count)

