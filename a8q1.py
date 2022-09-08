##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import treenode as tn
import treefunctions as tf

tp = list()
def count_node_types(tnode):

    if tnode is not None:
        if tf.is_leaf(tnode):
            tp.append(tnode)

        else:
            count_node_types(tn.get_left(tnode))
            count_node_types(tn.get_right(tnode))
        return tuple(tp)



def copy(tnode):
    if tnode is None:
        return None
    else:
        newtnode=tn.create(tn.get_data(tnode), copy(tn.get_left(tnode)), copy(tn.get_right(tnode)))
        return newtnode



def colect_data_inorder(tnode):
    if tnode is None:
        return [ ]
    else:
        return (collect_data_inorder(tn.get_left(tnode)) + [tn.get_data(tnode)] + collect_data_inorder(tn.get_right(tnode)))


def alter_subtrees(tnode, left_tree_offset, right_tree_offset, root_offset=0):
    if tnode is None:
        return None
    else:

        tn.set_left(tnode, tn.get_left(tnode)+ left_tree_offset)
        tn.set_left(tnode, tn.get_right(tnode) + right_tree_offset)
        return alter_subtrees(tnode, left_tree_offset, right_tree_offset, root_offset= tn.get_data(tnode))



