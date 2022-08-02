# # 一個存儲Trie節點的類
class Trie:
    #構造函數
    def __init__(self):
        self.isLeaf = False
        self.children = {}
        self.value = None
 
    #迭代函數將字符串插入Trie
    def insert(self, key):
        #從根節點開始
        curr = self
 
        #為每個字符做key
        for c in key:
            # 轉到下一個節點，如果路徑不存在則創建一個
            curr = curr.children.setdefault(c, Trie())
 
        # 將當前節點標記為葉子
        curr.isLeaf = True
        curr.value = key

 
    # 在 Trie 中搜索鍵的迭代函數。它返回真
    # 如果在 Trie 中找到密鑰，則為 #；否則，它返回 False
    def search(self, key):
        curr = self
 
        #為每個字符做key
        for c in key:
            # 去下一個節點
            curr = curr.children.get(c)
            # 如果字符串無效(到達 Trie 中路徑的末尾)
            if curr is None:
                return False
 
        # 如果當前節點是葉節點，則返回 true，並且我們已經到達
        # 字符串結束
        return curr.isLeaf