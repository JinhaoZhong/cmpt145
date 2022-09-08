##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import treenode as tn


def ordered(tnode, mini=None, maxi=None):
    """
    Purpose:
        Check if the tree are ordered.
    Preconditions:
        :param tnode: a treenode
    Return
        :return: True if the tree are ordered, False otherwise
    """
##empty tree is order
    if  tnode is None:
        return True
    data = tn.get_data(tnode)
##check not empty tree
    if (mini and data < mini) or (maxi and data > maxi):
        return False
    else:
        left = ordered(tn.get_left(tnode), mini, data - 1)
        right = ordered(tn.get_right(tnode), data + 1, maxi)
        return left and right



