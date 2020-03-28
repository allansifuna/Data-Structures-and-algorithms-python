class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.val}"


class BinTree(object):
    def minval(self, root):
        # print(root.val)
        if root.left is None:
            return root
        else:
            return self.minval(root.left)

    def insert(self, root, node):
        if root is None:
            return node
        else:
            if root.val < node.val:
                root.right = self.insert(root.right, node)
            else:
                root.left = self.insert(root.left, node)
        return root

    def inorder(self, root):
        if root is None:
            return None
        else:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return None
        else:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return None
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def delete(self, root, node):
        if root == None:
            return None

        if node.val < root.val:
            root.left = self.delete(root.left, node)
        elif node.val > root.val:
            root.right = self.delete(root.right, node)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return remp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minval(root)

            root.val = temp.val
            root.right = self.delete(root.right, temp)
        return root

    def levelorder(self, root):
        q = [root]
        for curr in q:
            if curr:
                print(curr.val, end=" ")

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

    def getheight(self, root):
        if root:
            left = self.getheight(root.left)
            right = self.getheight(root.right)
            if right > left:
                return right + 1
            else:
                return left + 1
        return -1


r = Node(5)
bst = BinTree()

a = [3, 2, 4, 6, 1, 8, 9]

for i in a:
    bst.insert(r, Node(i))

bst.preorder(r)
print()
bst.inorder(r)
print()
bst.postorder(r)
bst.delete(r, Node(5))
print()
bst.levelorder(r)
print()
print(bst.getheight(r))

print(bst.minval(r))
