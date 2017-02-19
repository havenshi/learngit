class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        l = []
        for p in places:
            if p != '..':
                l.append(p)
            else:
                if len(l) > 0:   # '..' means return parent path
                    l.pop()

        return '/' + '/'.join(l)

if __name__ == "__main__":
    answer=Solution()
    print answer.simplifyPath("/..")
