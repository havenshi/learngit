class Solution(object):
    def isPrime(self, integer):
        i=2
        while i<integer:
            if integer%i==0:
                return False
            else:
                i+=1

        return True

    def printPrime(self,n):
        i=2
        while i<=n:
            if self.isPrime(i)==True:
                print i,
            i+=1

if __name__ == "__main__":
    n = 200
    answer = Solution()
    print answer.printPrime(n)