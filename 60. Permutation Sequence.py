class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
    # method 1 time limit exceeded
    #     self.result = []
    #     nums=[i for i in range(1,n+1)]
    #
    #     for i in range(len(nums)):
    #         self.recursive_comb([nums[i]], nums[:i] + nums[i + 1:], n)
    #     return (self.result)[k-1]
    #
    # def recursive_comb(self,temp_array, rest_array, target):
    #     if len(temp_array) == target:
    #         if temp_array not in self.result:
    #             strtemp_array = ''.join([str(i) for i in temp_array]) # transfer list to string
    #             self.result.append(strtemp_array)
    #     else:
    #         for i in range(len(rest_array)):
    #             temp_array2 = temp_array[:]
    #             temp_array2.append(rest_array[i])
    #             self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target)

    # method 2
    # if n=3, we have (3-1)! start with 1/2/3, and for 1/2/3+left part, left part have (2-1)! start with what is left
    # check the region that the sequence number falls in and get the starting digit
        elements = range(1, n + 1)
        NN = reduce(lambda x, y: x * y, elements)  # n!
        k, result = k - 1, ''  # k is starting digit
        while len(elements) > 0:
            NN = NN / len(elements)  # the length of  the remain part, NN / len(elements)=(n-1)!
            i, k = k / NN, k % NN    # i is index of the value of this loop, k is how many k left
            result += str(elements.pop(i)) # delete the used item from element
        return result


if __name__ == "__main__":
    answer=Solution()
    print repr(answer.getPermutation(3,5))
