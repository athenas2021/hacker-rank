class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        # Se chegou ao final, retorna 0
        if root.left == None and root.right == None:
            return 0
        # inicializa profundidade para esquerda e direita
        lDepth = rDepth = 0
        # se tiver um nodo a esquerda, adiciona profundidade
        if root.left != None:
            lDepth = 1 + self.getHeight(root.left) 
        # se tiver um nodo a esquerda, adiciona profundidade
        if root.right != None:
            rDepth = 1 + self.getHeight(root.right)
        
        # Retorna o maior valor entre profundidade para esquerda e direita
        return max(lDepth, rDepth)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       