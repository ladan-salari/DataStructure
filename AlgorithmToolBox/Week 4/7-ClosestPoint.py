from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return sqrt((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)

def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")
    if len(points) <= 3:
        for i, j in combinations(points, 2):
            min_distance_squared = min(min_distance_squared,
                                       distance_squared(i, j))

    else:
        x_sorted = sorted(points)
        mid = len(x_sorted)//2
        min_zone1 = minimum_distance_squared_naive(x_sorted[:mid])
        min_zone2 = minimum_distance_squared_naive(x_sorted[mid+1:])
        min_d = min(min_zone1, min_zone2)
        min_d2 = middleZone(x_sorted, min_d)
        min_distance_squared = min(min_d, min_d2)

    return min_distance_squared

def middleZone(x_sorted, min_d):
    mid = len(x_sorted) // 2
    mid_value = x_sorted[mid][0]
    mid_zone =[]
    for point in x_sorted:
        if abs(point[0]-mid_value) < min_d:
            mid_zone.append(point)
    y_sorted = sorted(mid_zone, key=lambda p:p[1])
    if len(y_sorted)<2:
        return min_d
    else:
        min_d2 = distance_squared(y_sorted[0], y_sorted[1])
        for i in range(len(y_sorted)-1):
            for j in range(i+1, min(i+7, len(y_sorted))):
                min_d2 = min(min_d2, distance_squared(y_sorted[i], y_sorted[j]))
        return min_d2

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(minimum_distance_squared_naive(input_points)))
