class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


class BST:

    def __init__(self):
        self.root = None

    def traversal(self,type):
        if(self.root == None):
            print("Tree Empty")
        else:
            if(type == "inorder"):
                self._inorderTraversal(self.root)
            elif(type == "postorder"):
                self._postorderTraversal(self.root)
            else:
                self._preorderTraversal(self.root)
    
    def _inorderTraversal(self,root):

        if(root == None):
            return
        self._inorderTraversal(root.left)
        print(root.data)
        self._inorderTraversal(root.right)

    def _preorderTraversal(self,root):

        if(root == None):
            return
        print(root.data)
        self._preorderTraversal(root.left)
        self._preorderTraversal(root.right)

    def _postorderTraversal(self,root):

        if(root == None):
            return
        self._postorderTraversal(root.left)
        self._postorderTraversal(root.right)
        print(root.data)

        


    def insert(self,data):
       
        if(self.root == None):
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,root):
        if(data<=root.data):
            if(root.left == None):
                root.left = Node(data)
            else:
                self._insert(data,root.left)
        else:
            if(root.right == None):
                root.right = Node(data)
            else:
                self._insert(data,root.right)

    def find(self,key):
        if(self.root == None):
            return False
        else:
            return self._find(key,self.root)
    
    def _find(self,key,root):
        if(root == None):
            return False
        elif(root.data == key):
            return True
        elif(key < root.data):
            return self._find(key,root.left)
        else:
            return self._find(key,root.right)

    def findMax(self):
        if(self.root == None):
            return None

        return self._findMax(self.root)

    def _findMax(self,root):

        if(root.right == None):
            return root.data
        
        return self._findMax(root.right)

    def findMin(self):
        if(self.root == None):
            return None

        return self._findMin(self.root)

    def _findMin(self,root):

        if(root.left == None):
            return root.data
        
        return self._findMin(root.left)

    def height(self):
        if(self.root == None):
            return -1
        return self._height(self.root)

    
    def _height(self,root):
        if(root == None):
            return -1

        lh = self._height(root.left)
        rh = self._height(root.right)

        return 1 + max(lh,rh)


        

        



t1 = BST()
t1.insert(10)
t1.insert(5)
t1.insert(1)
t1.insert(15)
t1.insert(20)
t1.insert(30)


t1.traversal("postorder")
print(t1.find(16))
print(t1.findMax())
print(t1.findMin())
print(t1.height())


        
            

    