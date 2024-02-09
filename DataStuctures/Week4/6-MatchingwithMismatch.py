# python3
#
# import sys
#
# def solve(k, text, pattern):
# 	return []
#
# for line in sys.stdin.readlines():
# 	k, t, p = line.split()
# 	ans = solve(int(k), t, p)
# 	print(len(ans), *ans)



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10==0 and x!=0):
            return False
        main_number = x
        new_number=0
        while main_number > new_number:
            new_number=new_number*10 + x%10
            print(new_number)
            x = x//10
            print(x)
        if main_number == new_number:
            return True
        else:
            return False

x=121
result = Solution()
print(result.isPalindrome(x))


