# CMPT 145: Primitive Binary Search Trees
# Defines functions for primitive Binary Search Tree data structure
#
# A Primitive Binary Tree is defined as follows:
# 1. The value None is a primitive binary tree;
#    None is an empty tree.
# 2. If lt and rt are primitive binary trees, and d is any value
#    TreeNode(d, lt, rt) is a primitive binary tree.

# A Primitive Binary Tree t satisfies the Binary Search Tree (BST)
# property if all of the following hold:
# 1. The key stored at TreeNode t is greater than any key
#    in t's left subtree (if any)
# 2. The key stored at TreeNode t is less than any key
#    in t's right subtree (if any)
# 3. t's left subtree satisfies the BST property
# 4. t's right subtree satisfies the BST property

#Jinhao Zhong, 11204178, CMPT145, lab05

import KVTreeNode as TN

def member_prim(tnode, key):
    """
    Purpose:
        Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        none
    :return: a pair True, value if key is in the tree
             a pair False, None if the key is not in the tree
    """
    if tnode is None:
        return False, None
    elif tnode.key is key:
        return True, tnode.value
    elif key < tnode.key:
        return member_prim(tnode.left, key)
    else:
        return member_prim(tnode.right, key)


def insert_prim(tnode, key, value):
    """
    Insert a new key,value into the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        If the key is not already in the tree, it is added.
        If the key is already in the tree, the old value is replaced
        with the given value.
    Return
        :return: tuple (flag, tree)
        flag is True if insertion succeeded;
                tree contains the new key-value
        flag is False if the value is already in the tree,
                the value stored with the key is changed
    """
    if tnode is None:
        return True, TN.KVTreeNode(key, value)
    else:
        if tnode.key == key:
            tnode.value = value
            return False, tnode
        elif key < tnode.key:
            left, lvalue=insert_prim(tnode.left, key, value)
            if left:
                tnode.left = lvalue
            return left, tnode

        else:
            right, rvalue=insert_prim(tnode.right, key, value)
            if right:
                tnode.right = rvalue
            return right, tnode





def delete_prim(tnode, key):
    """
    Delete a value from the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        If the key is in the tree, it is deleted.  The tree
        retains the binary search tree property.
        If the key is not there, there is no change to the tree.
    Return
        :return: tuple (flag, tree)
        flag is True if deletion succeeded;
                tree is the resulting without the value
        flag is False if the value was not in the tree,
                tree returned unchanged
    """
    if tnode is None:
        return False, None
    else:
        if tnode.key == key:
            if tnode.left is None and tnode.right is None:
                return True, None
            elif tnode.left is None:
                return True, tnode.left
            elif tnode.right is None:
                return True, tnode.right
            else:
                temp = tnode.left
                while temp.right is not None:
                    temp =temp.right
                temp.right = tnode.right
                return True, tnode.left
        elif tnode.key>key:
            flag, temp = delete_prim(tnode.left, key)
            if flag:
                tnode.left= temp
            return flag, tnode
        else:
            flag, temp = delete_prim(tnode.right, key)
            if flag:
                tnode.right = temp
        return flag, tnode



