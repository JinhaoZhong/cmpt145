# CMPT 145: Assignment 5 Question 3

import node as node
import a5q2 as a5q2


def contains_duplicates(node_chain):
    """
    Purpose:
        Returns whether or not the given node_chain contains one or more duplicate data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Return:
        :return: True if duplicate data value(s) were found, False otherwise
    """

##return false if the chain is empty
    walker = node_chain
    if a5q2.count_chain(walker) == 0:
        return False

##check if the duplicates chain the same as the original chain
    nodes = []  ##create a new list to save data
    while walker is not None:
        data = node.get_data(walker)
        if data in nodes:
            return True
        nodes.append(data)
        walker = node.get_next(walker)
    return False


def reverse_chain(node_chain):
    """
    Purpose:
        Completely reverses the order of the given node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Post-conditions:
        The front of the node_chain is altered to be the back, with all nodes now pointing next the opposite direction.
    Return:
        :return: The resulting node chain that has had its order reversed
    """

##return a empty node chain
    walker=node_chain
    if a5q2.count_chain(walker)<=1:
        return walker

##reverse the node chain if it is not empty
    list=[] ## create a list to save data
    while walker is not None:
        list.append(node.get_data(walker))
        walker = node.get_next(walker)
    walker=node_chain

##set data in list into node chain
    x = len(list)-1
    while walker is not None:
        node.set_data(walker,list[x])
        walker=node.get_next(walker)
        x-=1

    return node_chain





def insert_value_sorted(node_chain, number_value):
    """
    Purpose:
        Insert the given number_value into the node-chain so that it appears after a previous value that is <= value. If the node_chain was empty, new value is simply placed at the front.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing only numbers
        :param number_value: a numerical value to be inserted
        Assumption:  node_chain only contains numbers (which can be compared to the given number_value)
    Post-condition:
        The node-chain is modified to include a new node with number_value as its data after a previous node's data value is <= number_value.
    Return
        :return: the node-chain with the new value in it
    """

##if  the node_chain is empty
    walker = node_chain
    if walker == None:
        walker = node.create(number_value, None)
        return walker

##if the number value if 0
    elif number_value == 0:
        return node_chain

##if there is only one chain and check if the number value greater or smaller than the node
    elif node.get_next(walker) == None:
        if node.get_data(walker) < number_value:
            node = node.create(number_value)
            node.set_next(walker, node)
            return walker
        else:
            walker = node.create(number_value, walker)
            return walker


    elif number_value <= node.get_data(walker):
        node = node.create(number_value, walker)
        return node

    while node.get_next(walker) is not None:
        if number_value >= node.get_data(walker):
            if number_value <= node.get_next(walker):
                node = node.create(number_value, node.get_next(walker))
                node.set_next(walker, node)
                return node_chain

    return node_chain


