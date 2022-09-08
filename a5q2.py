# CMPT 145: Assignment 5 Question 2

import node as node



def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """

##return 0 if the node chain is empty
    if node_chain is None:
        return 0

##count the node chain if it is not empty
    else:
        return count_chain(node.get_next(node_chain)) + 1


def delete_front_nodes(node_chain, n):
    """
    Purpose:
        Deletes the first n nodes from the front of the node chain.
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param n: integer, how many nodes that should be removed off the front of the node chain
    Post-conditions:
        The node-chain is changed, by removing the first n nodes. If n>length of node_chain, node_chain is set to be empty (None)
    Return:
        :return: The resulting node chain, which may now be empty (None)
    """

##if node chain is empty, nothing to delete
    if node_chain is None:
        return None

##delete the front node chain if it is not empty
    else:
        return delete_front_nodes(node.get_next(node_chain), n - 1)


def replace_last(node_chain, target_val, replacement_val):
    """
    Purpose:
        Replaces the last occurrence of target data value with the new_value. The chain should at most have 1 data value changed.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
        :param target_val: the target data value we are searching to replace the last instance of
        :param replacement_val: the data value to replace the target_val that we found
    Post-conditions:
        The node-chain is changed, by replacing the last occurrence of target_val. If target_val is not present, then the node_chain returns unaltered.
    Return:
        :return: The altered node chain where any data occurrences of target_val has been replaced with replacement_val.
    """

    node_chain1 = None
    walker = node_chain

##find the last node
    while walker is not None:
        if node.get_data(walker) == target_val:
            node_chain1 = walker
        walker = node.get_next(walker)

## replace the target value
    if node_chain1 is not None:
        node.set_data(node_chain1, replacement_val)

    return walker