# coding=utf-8
class Trie:
    root = {}
    END = '/'

    def add(self, word):
        # 从根节点遍历单词,char by char,如果不存在则新增,最后加上一个单词结束标志
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node