##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import treenode as tnode


def weigh_tree(root):
    def summed(root):
        if root is None:
            return 0
        else:
            return root['data'] + summed(root['left']) + summed(root['right'])

    return (summed(root['left']),root['data'],summed(root['right']))




