# # python3
#
import sys

class Solver:
	def __init__(self, s):
		self.s = s

	def PolyHash(self, s, prime, multiplier):
		hashlib = list([] for _ in range(len(s)+1))
		hashlib[0] = 0
		for i in range(1, len(s)+1):
			hashlib[i] = (hashlib[i-1] * multiplier + ord(s[i-1])) % prime
		return hashlib

	def Power(self, length, multiplier,  prime):
		pow1 = list([] for _ in range(len(s)+1))
		pow1[0]= 0
		for i in range(1, length+1):
			pow1[i] = pow(multiplier, i, prime)
		return pow1


	def Hashval(self, hashlib, prime, start, length, y):
		hashvalue = (hashlib[start+length] - y*hashlib[start]) % prime
		return hashvalue

	def ask(self, hashlib1, hashlib2, prime1, prime2, a, b, l, y1, y2):
		hasha1 = self.Hashval(hashlib1, prime1, a, l, y1)
		hasha2 = self.Hashval(hashlib2, prime2, a, l, y2)
		hashb1 = self.Hashval(hashlib1, prime1, b, l, y1)
		hashb2 = self.Hashval(hashlib2, prime2, b, l, y2)
		if hasha1 == hashb1 and hasha2 == hashb2:
			return True
		else:
			return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
multiplier = 263
prime1 = 1000000007
prime2 = 1000000009
y1 = solver.Power(len(s), multiplier, prime1)
y2 = solver.Power(len(s), multiplier, prime2)
hashlib1 = solver.PolyHash(s, prime1, multiplier)
hashlib2 = solver.PolyHash(s, prime2, multiplier)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(hashlib1, hashlib2, prime1, prime2, a, b, l, y1[l], y2[l]) else "No")

### To reduce the probability of collision we comupte hash value for two different modular. Which
### reduce the probablitiy of collision