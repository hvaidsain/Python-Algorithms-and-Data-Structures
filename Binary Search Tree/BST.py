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


        



t1 = BST()
t1.insert(10)
t1.insert(5)
t1.insert(15)
t1.traversal("postorder")
print(t1.find(16))

        
            

    