class Solution(object):
    def isPrime(self, integer):
        i=2
        while i<integer:
            if integer%i==0:
                return False
            else:
                i+=1

        return True

if __name__ == "__main__":
    integer = 46
    answer = Solution()
    print answer.isPrime(integer)