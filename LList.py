##CMPT154, Jinhao Zhong, jiz263, 11204178

# CMPT 145: Node-Based Data Structures
# Defines the Linked List ADT
#
# Here we re-invent Python's built-in lists.  We will provide a subset of
# the operations that a Python list provides.
#
# Implementation:
#   This implementation uses the linked node structure.

import node as node


def create():
    """
    Purpose
        creates an empty list
    Return
        :return an empty list
    """
    llist = {}
    llist['size'] = 0     # how many elements in the stack
    llist['head'] = None  # the node chain starts here; initially empty
    llist['tail'] = None
    return llist


def is_empty(alist):
    """
    Purpose
        Checks if the given list has no data in it
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return True if the list has no data, or False otherwise
    """

##return True if it is empty, False otherwise
    if alist['size'] == 0:
        return True
    else:
        return False



def size(alist):
    """
    Purpose
        Returns the number of data values in the given list
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return The number of data values in the list
    """
    return alist['size']


# TODO: complete add_to_front(alist, val)  --- when done, delete this line
def add_to_front(alist, val):
    """
    Purpose
        Insert val into alist at the front of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is at index 0.
        The values previously in the list appear after the new value.
    Return:
        :return None
    """

##create a newnode
    newnode = node.create(val, alist['head'])
    alist['head'] = newnode

##if the list is empty
    if alist['tail'] is None:
        alist['tail'] = newnode
    alist['size']+=1
    return alist




def add_to_back(alist, val):
    """
    Purpose
        Insert val into alist at the end of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is last in the list.
    Return:
        :return None
    """

##create a newnode
    newnode = node.create(val, None)

##if the list is empty, head and tail are the same as the new node
    if alist['size'] == 0:
        alist['head'] = newnode
        alist['tail'] = newnode

##add the newnode to the front if the list is not empty
    else:
        node.set_next(alist['tail'], newnode)
        alist['tail'] = newnode
    alist['size'] += 1
    return alist



def value_is_in(alist, val):
    """
    Purpose
        Check if the given value is in the given list
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True if the value is in the list, False otherwise
    """

##create a new node
    newnode = alist['head']

##check if the value in alist, return True if it is, false otherwise
    while newnode is not None:
        if node.get_data(newnode) == val:
            return True
        newnode = node.get_next(newnode)
    return False



def get_index_of_value(alist, val):
    """
    Purpose
        Return the smallest index of the given val in the given alist.
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return the tuple (True, idx) if the val appears in alist
        :return the tuple (False, None) if the vale does not appear in alist
    """

## return False if alist is empty
    if alist is None:
        return False, None

##get the index of value
    else:
        idx = 0
        checknode=alist['head']
        while checknode is not None:
            if node.get_data(checknode) == val:
                return True, idx
            idx += 1
            checknode=node.get_next(checknode)
        return False, None



def retrieve_data_at_index(alist, idx):
    """
    Purpose
        Return the value stored in alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        none
    Return:
        :return (True, val) if val is stored at index idx and idx is valid
        :return (False, None) if the idx is not valid for the list
    """

##If alist is empty, return False
    if alist['size'] == 0:
        return False, None

##return the data at index, False if index is larger than alist size
    else:
        if idx<alist['size'] and idx is not None:
            index = 0
            checknode= alist['head']
            while checknode is not None:
                if index == idx:
                    return True, node.get_data(checknode)
                index += 1
            return True, checknode
        return False, None



def set_data_at_index(alist, idx, val):
    """
    Purpose
        Store val into alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a non-negative integer
    Post-conditions:
        The value stored at index idx changes to val
    Return:
        :return True if the index was valid, False otherwise
    """

##return False if the alist size is 0
    if alist['size'] == 0:
        return False

##set the data in alist at index, False if index is too large or too small
    else:
        if idx is not None and idx<=alist['size']:
            index = 0
            tempnode = alist['head']
            while tempnode is not None:
                if index == idx:
                    node.set_data(tempnode, val)
                    return True
                else:
                    tempnode = node.get_next(tempnode)
                    index += 1

            return False



def remove_from_front(alist):
    """
    Purpose
        Removes and returns the first value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """

##return False if alist is empty
    if alist['head'] is None:
        return False, None

##remove the front node, return False if there is nothing to remove
    else:
        remove= node.get_data(alist['head'])
        alist['head'] = node.get_next(alist['head'])
        alist['size'] -= 1
        return True, remove
    return False, None


def remove_from_back(alist):
    """
    Purpose
        Removes and returns the last value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
##return False if there is nothing to remove
    if alist['tail'] is None:
        return False, None

    else:
        tempnode = alist['head']
        nextnode = node.get_next(tempnode)
##when there is only one node in alist
        if nextnode is None:
            val = node.get_data(tempnode)
            alist['head'] = alist['tail'] = None
            alist['size'] = 0
            return True, val
##When there are more than one node in aist
        while nextnode != alist['tail']:
            tempnode = nextnode
            nextnode = node.get_next(nextnode)
        val = node.get_data(alist['tail'])
        node.set_next(tempnode, None)
        alist['size'] -= 1
        alist['tail'] = tempnode
        return True, val
    return False, None



def insert_value_at_index(alist, val, idx):
    """
    Purpose
        Insert val into alist at index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a valid index for the list
    Post-conditions:
        The list increases in size.
        The new value is at index idx.
        The values previously in the list at idx or later appear after the new value.
        If the given index == size of list, simply insert the new value at the end of the list.
    Return:
        :return If the index is valid, insert_value_at_index returns True.
        :return If the index is not valid, insert_value_at_index returns False.
    """

##if index is correct, insert value, False otherwise
    if idx>0 and idx<=alist["size"]:
        if idx == 0:
            add_to_front(alist, val)
            return True
        elif idx == alist['size']:
            add_to_back(alist, val)
            return True
        else:
            tempnode = alist['head']
            i = 0
            while i <idx-1:
                tempnode= node.get_next(tempnode)
                i+=1
            newnode = node.create(val, node.get_next(tempnode))
            node.set_next(tempnode, newnode)
            alist['size']+=1
            return True

##if alist size is 0 and idx in None
    elif alist['size']==0:

        return True
    return False


def delete_item_at_index(alist, idx):
    """
    Purpose
        Delete the value at index idx in alist.
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        The list decreases in size if the index is valid
        The value at idx is no longer in the list.
    Return:
        :return True if index was valid, False otherwise
    """

##check idx, if it doen't fit, return False
    if idx <0 or idx >alist['size']:
        return False

##remove the value ar index
    else:
        if idx == 0:
            remove_from_front(alist)
            return True
        elif idx== alist['size']:
            remove_from_back(alist)
            return True
        else:
            i = 0
            tempnode = alist['head']
            while i< idx-1:
                tempnode=node.get_next(tempnode)
                i+=1


            alist['size'] -= 1
            return True

    return False


