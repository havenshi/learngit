class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for item in strs:
            order = ("".join(sorted(item))).lower()
            if order not in map:
                map[order] = [item.lower()]
            else:
                map[order] += [item.lower()]

        l = []
        for i in map.keys():
            l.append(map[i])
        return l

if __name__ == "__main__":
    answer=Solution()
    print answer.groupAnagrams(["Eat", "tea", "tan", "ate", "nat", "bat"])
