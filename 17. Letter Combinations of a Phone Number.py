class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {"2": ["a", "b", "c"],
               "3": ["d", "e", "f"],
               "4": ["g", "h", "i"],
               "5": ["j", "k", "l"],
               "6": ["m", "n", "o"],
               "7": ["p", "q", "r", "s"],
               "8": ["t", "u", "v"],
               "9": ["w", "x", "y", "z"]}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            mylist = []
            for i in map[digits]:
                mylist.append(i)
            return mylist
        else:
            newlist = []
            for i in map[digits[0]]:
                for j in self.letterCombinations(digits[1:]):
                    newlist.append(i+j)
            return newlist

if __name__ == "__main__":
    answer=Solution()
    print answer.letterCombinations("5678")
