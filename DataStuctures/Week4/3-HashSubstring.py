# # python3
# this is also works but the other solution is more universal
# def read_input():
#     return (input().rstrip(), input().rstrip())
#
# def print_occurrences(output):
#     print(' '.join(map(str, output)))
#
# def get_occurrences(pattern, text):
#     return [
#         i
#         for i in range(len(text) - len(pattern) + 1)
#         if text[i:i + len(pattern)] == pattern
#     ]
#
# if __name__ == '__main__':
#     print_occurrences(get_occurrences(*read_input()))


# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def PolyHash(s, prime, multiplier):
    hash = 0
    for i in range(len(s)-1, -1, -1):
        hash = (hash*multiplier + ord(s[i])) % prime
    return hash

def PrecomputeHashes(pattern, text, prime, multiplier):

    Hash = list([] for _ in range(len(text)-len(pattern)+1))
    s = text[len(text)-len(pattern):]
    Hash[len(text)-len(pattern)] = PolyHash(s, prime, multiplier)
    y = 1
    for i in range(1, len(pattern)+1):
        y = (y*multiplier)%prime
    for i in range(len(text)-len(pattern)-1, -1, -1):
        Hash[i] = (multiplier*Hash[i+1] + ord(text[i]) - y*ord(text[i+len(pattern)]))%prime
    return Hash

def RabinKarp(pattern, text):
    prime = 1000000007
    multiplier = 236
    position = []
    pHash = PolyHash(pattern, prime, multiplier)
    H = PrecomputeHashes(pattern, text, prime, multiplier)
    for i in range(len(text)-len(pattern)+1):
        if pHash == H[i]:
            position.append(i)
    return position


if __name__ == '__main__':
    result = RabinKarp(*read_input())
    for i in result:
        print(str(i), end=' ')

