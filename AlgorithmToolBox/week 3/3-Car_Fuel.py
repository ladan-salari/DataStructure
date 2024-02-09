from sys import stdin


def min_refills(distance, tank, stops):
    number_stop =0
    if distance <= tank:
        return 0
    if distance - stops[-1] > tank:
        return -1
    if len(stops) ==1:
        if distance-stops[0] <=tank:
            return 1
    for i in range(len(stops)-1):
        if stops [i+1] - stops[i] > tank:
            return -1
    loc_distance = 0
    for i in range(len(stops)-1):
        if stops[i] <= loc_distance + tank and stops[i+1]> loc_distance +tank:
            number_stop += 1
            loc_distance = stops[i]
        if loc_distance + tank < distance and i == len(stops)-2:
            number_stop +=1
            loc_distance = stops[i+1]
        if loc_distance + tank >= distance:
            return number_stop


    # write your code here


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
## Still doesn't pass the test
