class Solution(object):
    def fibonacci(self,n):
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return self.fibonacci(n-2)+self.fibonacci(n-1)

if __name__ == "__main__":
    n = 10
    answer = Solution()
    print answer.fibonacci(n)
