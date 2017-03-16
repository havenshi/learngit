import Queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
    #     l = [beginWord] + wordList
    #     count = [0] * (len(l))
    #     count[0] = 1
    #     for i in range(1, len(l)):
    #         if l[i] == l[0]:  # if item equals to beginword, set it 1
    #             count[i] = 1
    #         for j in range(i):        # compare with all the element before j
    #             if self.compare(l[i], l[j]):  # if only one item is different
    #                 if count[j] != 0:   # count[j] == 0 means cannot cross this position
    #                     if count[i] == 0:  # there must be 1 way to reach this position
    #                         count[i] = count[j] + 1
    #                     else:
    #                         count[i] = min(count[i], count[j] + 1)   # min of count[i] itself and count[j] + 1
    #     print count
    #     for i in range(len(l)-1,0,-1):
    #         for j in range(len(l)-1,i,-1):
    #             if self.compare(l[i], l[j]):
    #                 if count[j] != 0:   # count[j] == 0 means cannot cross this position
    #                     if count[i] == 0:  # there must be 1 way to reach this position
    #                         count[i] = count[j] + 1
    #                     else:
    #                         count[i] = min(count[i], count[j] + 1)   # min of count[i] itself and count[j] + 1
    #     if endWord not in l:
    #         return 0
    #     print count
    #     return count[l.index(endWord)]
    #
    # def compare(self, before, after):
    #     if len(before) == len(after):
    #         count = 0
    #         for i in range(len(before)):
    #             if before[i] != after[i]:
    #                 count += 1
    #         if count == 1:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

        wordSet = set([])
        for item in wordList:
            wordSet.add(item)   # transfer list into set
        queue = Queue.Queue()
        queue.put(beginWord)
        goal = {beginWord:1}
        char = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # character list a~z
        while not queue.empty():  # BFS
            cur = queue.get()  # FIFO
            if cur == endWord:
                return goal[cur] # base
            while cur in wordSet:
                wordSet.remove(cur)  # remove duplicate
            for i in range(len(cur)):  # tranverse each position of current word
                p1 = cur[:i]
                p2 = cur[i + 1:]
                for j in char:
                    word = p1 + j + p2
                    if word in wordSet:
                        queue.put(word)
                        goal[word] = goal[cur] + 1  # new item, step + 1
                        wordSet.remove(word)  # important! if visited, should not visit again, so delete.
        return 0

if __name__ == "__main__":
    answer=Solution()
    print answer.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])