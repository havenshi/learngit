class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

class TreeNode:
   def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):   # replace the node value
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self  # point parent of left to self
        if self.hasRightChild():
            self.rightChild.parent = self


# put method
def put(self,key,val):
    if self.root:            # if root exists, use help function
        self._put(key,val,self.root)
    else:
        self.root = TreeNode(key,val) # if no root, create a new treenode
    self.size = self.size + 1

def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():   # if has left, use recursion to search left child
               self._put(key,val,currentNode.leftChild)
        else:
               currentNode.leftChild = TreeNode(key,val,parent=currentNode) # if not has left, set the value as a left child
    else:
        if currentNode.hasRightChild():  # search right
               self._put(key,val,currentNode.rightChild)
        else:
               currentNode.rightChild = TreeNode(key,val,parent=currentNode)

def __setitem__(self,k,v):   # call the put method
    self.put(k,v)


# get method
def get(self,key):
    if self.root:
        res = self._get(key,self.root)
        if res:                    # if find the node that key==target, return its payload.
               return res.payload  # When a matching key is found, the value stored in the payload of the node is returned.
        else:
               return None
    else:
        return None

def _get(self,key,currentNode):
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return self._get(key,currentNode.leftChild)
    else:
        return self._get(key,currentNode.rightChild)

def __getitem__(self,key):  # call the get method
    return self.get(key)


# delete method
def delete(self,key):
   if self.size > 1:
      nodeToRemove = self._get(key,self.root)
      if nodeToRemove:
          self.remove(nodeToRemove)
          self.size = self.size-1
      else:
          raise KeyError('Error, key not in tree')
   elif self.size == 1 and self.root.key == key:
      self.root = None
      self.size = self.size - 1
   else:
      raise KeyError('Error, key not in tree')

def __delitem__(self,key):
    self.delete(key)


def remove(self, currentNode):
    if currentNode.isLeaf():    # 1.The node to be deleted has no children
        if currentNode == currentNode.parent.leftChild:
            currentNode.parent.leftChild = None
        else:
            currentNode.parent.rightChild = None

    elif currentNode.hasBothChildren():  # 3.The node to be deleted has two children
        succ = currentNode.findSuccessor()
        succ.spliceOut()
        currentNode.key = succ.key
        currentNode.payload = succ.payload

    else:                       # 2.The node to be deleted has only one child
        if currentNode.hasLeftChild():  # point left's parent to current's parent, and promote parent's left to current's left
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChild
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.leftChildh
            else:
                currentNode.replaceNodeData(currentNode.leftChild.key,  # replace
                                            currentNode.leftChild.payload,
                                            currentNode.leftChild.leftChild,
                                            currentNode.leftChild.rightChild)
        else:
            if currentNode.isLeftChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
            else:
                currentNode.replaceNodeData(currentNode.rightChild.key,
                                            currentNode.rightChild.payload,
                                            currentNode.rightChild.leftChild,
                                            currentNode.rightChild.rightChild)

# 3.The node to be deleted has two children, swap the node with the next-largest node(successor)
# If the node has a right child, then the successor is the smallest key in the right subtree.
# If the node has no right child and is the left child of its parent, then the parent is the successor.
# If the node is the right child of its parent, and itself has no right child, then the successor to this node is the successor of its parent, excluding this node.
def findSuccessor(self):
    succ = None
    if self.hasRightChild():
        succ = self.rightChild.findMin()
    else:
        if self.parent:
               if self.isLeftChild():
                   succ = self.parent
               else:
                   self.parent.rightChild = None
                   succ = self.parent.findSuccessor()
                   self.parent.rightChild = self
    return succ

def findMin(self):
    current = self
    while current.hasLeftChild():
        current = current.leftChild
    return current

def spliceOut(self):
    if self.isLeaf():
        if self.isLeftChild():
               self.parent.leftChild = None
        else:
               self.parent.rightChild = None
    elif self.hasAnyChildren():
        if self.hasLeftChild():
               if self.isLeftChild():
                  self.parent.leftChild = self.leftChild
               else:
                  self.parent.rightChild = self.leftChild
               self.leftChild.parent = self.parent
        else:
               if self.isLeftChild():
                  self.parent.leftChild = self.rightChild
               else:
                  self.parent.rightChild = self.rightChild
               self.rightChild.parent = self.parent