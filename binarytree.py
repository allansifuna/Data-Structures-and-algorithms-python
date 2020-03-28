class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"{self.data}"


class BinaryTree(object):

    def insert(self, root, node):
        if root is None:
            return node
        else:
            if root.data < node.data:
                root.right_child = self.insert(root.right_child, node)
            else:
                root.left_child = self.insert(root.left_child, node)
        return root

    def minValueNode(self, node):
        current = node
        # loop down to find the leftmost leaf
        while(current.left_child is not None):
            current = current.left_child
        return current

    def delete(self, root, node):
        if root == None:
            return None
        if node.data < root.data:
            root.left_child = self.delete(root.left_child, node)
        elif node.data > root.data:
            root.right_child = self.delete(root.right_child, node)
        else:
            if root.left_child == None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root.left_child = None
                return temp
            temp = self.minValueNode(root.right_child)
            # Copy the inorder successor's content to this node
            root.data = temp.data
            # Delete the inorder successor
            root.right = self.delete(root.right_child, temp)
        return root

    def preorder(self, root):
        if root is None:
            return None
        else:
            print(root.data, end=" ")
            self.preorder(root.left_child)
            self.preorder(root.right_child)

    def getHeight(self, root):
        if root:
            leftDepth = self.getHeight(root.left_child)
            rightDepth = self.getHeight(root.right_child)

            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
        else:
            return -1

    def post_order(self, root):
        if not root:
            return None
        else:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            print(root.data, end=" ")

    def levelOrder(self, root):
        q = [root]
        for current in q:
            if current:
                print(current.data, end=' ')
                if current.left_child:
                    q.append(current.left_child)
                if current.right_child:
                    q.append(current.right_child)

    def in_order(self, root):
        if root:
            self.in_order(root.left_child)
            print(root.data, end=" ")
            self.in_order(root.right_child)

    def __str__(self):
        return self.levelOrder()


r = Node(5)
# bst = BinaryTree()
# a = [1, 2, 4, 3, 7, 6, 10, 0, 9]
# for i in a:
#     bst.insert(r, Node(i))

# bst.delete(r, r)
# bst.preorder(r)
# print()
# bst.in_order(r)
# print()
# bst.post_order(r)
# print()
# bst.levelOrder(r)

bst = BinaryTree()


def restoreTree(inorder, preorder, r):
    for i in inorder:
        bst.insert(r, Node(i))

    return bst


# 6 1 0 2 4 3 7 10 9
# 0 1 2 3 4 6 7 9 10
# 0 3 4 2 1 9 10 7 6
# 6 1 7 0 2 10 4 9 3
a = [1, 0, 2, 4, 3, 7, 10, 9]
b = [0, 1, 2, 3, 4, 7, 9, 10]
f = Node(6)
tr = restoreTree(b, a, r)
tr.levelOrder(r)
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def find_max(t, parent):
    """
    Traverse a binary tree to find its max (far right)
    :param t: root of the tree
    :return: the max node
    """
    while t.right:
        parent = t
        t = t.right
    return t, parent


def delete_bst_nodes(t, value):
    """
    Delete value node from  a binary tree and preserve BST property.
    - Traverse the tree to find the node to delete;
    - If found:
        1) Node has no children, just return None to the caller (which set
        its left/right node to the returned None)
        2) Node has one child, just return the child to the caller (which set
        its left/right node to the returned child and thus detach the node to delete)
        3) Node has both children:
           - Find the max in left subtree (min in right subtree would work too)
           - Make the value of the node to delete as the max just found
           - Remove the above duplicated node from the subtree
           - Return the root of the subtree, which now doesn't contain the deleted node
    :param t: Root of the tree
    :param value: The value to delete
    :return: Root of the tree, without the deleted node if found
    """
    if not t:
        return t

    # Value is in left subtree
    if t.value > value:
        t.left = delete_bst_nodes(t.left, value)
    # Value is in right subtree
    elif t.value < value:
        t.right = delete_bst_nodes(t.right, value)
    # Value is this node!
    else:
        # If no children, None will be returned to the caller
        # This means t.left or t.right of the caller will be set to None
        # And so this node is detached (removed)
        if not t.left and not t.right:
            return None
        # No left child, return right child
        # This means t.left or t.right of the caller will be set to right child
        # And so this node is detached (removed)
        elif not t.left:
            return t.right
        # Both children exists
        else:
            # Find max of left node to keep BST property (min of right node would work too)
            max_of_left, parent = find_max(t.left, t)

            # Set the left subtree of this cloned node with the current left subtree head
            # after removing the duplicated/cloned node from it
            if parent == t:
                parent.left = max_of_left.left
            else:
                parent.right = max_of_left.left
            # Clone the value into this node
            t.value = max_of_left.value
    return t


def deleteFromBST(t, queries):
    for value_to_rm in queries:
        t = delete_bst_nodes(t, value_to_rm)
    return t
