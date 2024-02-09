# python3

import sys
from collections import namedtuple


# Answer = namedtuple('answer_type', 'i j len')


def PolyHash(s, prime, multiplier):
    hash_value = 0
    for i in range(len(s) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(s[i])) % prime
    return hash_value

def PrecomputeHashes(text, pattern_length, prime, multiplier):
    Hash = list([] for _ in range(len(text) - pattern_length + 1))
    s = text[len(text) - pattern_length:]
    Hash[len(text) - pattern_length] = PolyHash(s, prime, multiplier)
    y = pow(multiplier, pattern_length, prime)
    for i in range(len(text) - pattern_length - 1, -1, -1):
        Hash[i] = (multiplier * Hash[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime
    return Hash


def PrecomputeHashDic(text, pattern_length, prime, multiplier):
    hash_D = {}
    sub_s = text[len(text) - pattern_length:]
    value = PolyHash(sub_s, prime, multiplier)
    hash_D[value] = len(text) - pattern_length
    y = pow(multiplier, pattern_length, prime)
    for j in range(len(text) - pattern_length - 1, -1, -1):
        current = (multiplier * value + ord(text[j]) - y * ord(text[j + pattern_length])) % prime
        hash_D[current] = j
        value = current
    return hash_D


def SearchSubstring(Hash, hash_D):
    check = False
    matches = {}
    for i in range(len(Hash)):
        start = hash_D.get(Hash[i], -1)
        if start != -1:
            check = True
            matches[i] = start
    return check, matches


def Maxlength(string1, string2, low, high, max_length, start1, start2, multiplier, prime1, prime2):
    if low > high:
        return start1, start2, max_length
    mid = (low + high) // 2
    hash1_1 = PrecomputeHashes(string1, mid, prime1, multiplier)
    hash1_2 = PrecomputeHashes(string1, mid, prime2, multiplier)
    hash2_1 = PrecomputeHashDic(string2, mid, prime1, multiplier)
    hash2_2 = PrecomputeHashDic(string2, mid, prime2, multiplier)
    check1, matches1 = SearchSubstring(hash1_1, hash2_1)
    check2, matches2 = SearchSubstring(hash1_2, hash2_2)
    if check1 and check2:
        for a, b in matches1.items():
            temp = matches2.get(a, -1)
            if temp != -1:
                max_length = mid
                start1, start2 = a, b
                del hash1_1, hash2_1, hash2_2, hash1_2, matches1, matches2
                return Maxlength(string1, string2, mid + 1, high, max_length, start1, start2, multiplier, prime1,
                                 prime2)
    return Maxlength(string1, string2, low, mid - 1, max_length, start1, start2, multiplier, prime1, prime2)


multiplier = 263
prime1 = 1000000007
prime2 = 1000004249

while True:
    line = input()
    if line == '':
        break
    else:
        s, t = line.split()
        if len(s) <= len(t):
            short_s, long_s = s, t
        else:
            short_s, long_s = t, s
        l, i, j = Maxlength(long_s, short_s, 0, min(len(s), len(t)), 0, 0, 0, multiplier, prime1, prime2)
        if len(s) <= len(t):
            print(i, l, j)
        else:
            print(l, i, j)
