# CMPT 145:  Binary Search Trees
#       Implements the Table ADT
#
# Data structure:
#   a table is a object containing two atributes:
#     'root'  - value stores the root of a primitive binary tree
#     'size'  - value stores the number of nodes in the primitive binary tree
# The methods ensure that the primitive binary tree satisfies the
# binary search tree property

#Jinhao Zhong, 11204178, CMPT145, lab05

import a9q2 as prim

class Table(object):
    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        """
        Purpose:
            Return the size of the table.
        Return:
            :return: the number of key,value pairs in the table
        """
        return self.__size

    def is_empty(self):
        """
        Purpose:
            Indicate whether the given table is empty.
        Return:
            :return: True if the table is empty
        """

        return self.__size == 0
    def retrieve(self, key):
        """
        Return the value associated with the given key.
        Preconditions:
            :param key: a key
        Postconditions:
            none
        Return
            :return: True, value if the key appears in the table
                     False, None otherwise
        """
        return prim.member_prim(self.__root, key)

    def insert(self, key, value):
        """
        Insert a new key, value into the table.
        Preconditions:
            :param key: a unique key for the value
            :param value: a value
        Postconditions:
            If the key is not already in the table, it is added to the table
            If the key is already there, change the value
        Return
            :return: True if the key,value was inserted
                     False if the value of an existing key was changed
        """
        flag, table =prim.insert_prim(self.__root, key, value)
        if flag:
            self.__root =table
            self.__size+=1
        return flag



    def delete(self, key):
        """
        Delete a given key and its associated value from the table.
        Preconditions:
            :param key: a unique key for the value
        Postconditions:
            If the key is not in the table, no change to the table
            If the key is in the table, remove it
        Return
            :return: True if the key,value was deleted
        """
        flag, table = prim.delete_prim(self.__root, key)
        if flag:
            self.__root =table
            self.__size -=1
        return flag

    def in_order(self):
        """
        Returns a string of the keys showing the in-order sequence
        """

        def in_order_prim(kvtnode):

            if kvtnode is None:
                return " "
            else:
                before = in_order_prim(kvtnode.left)
                this = '('+str(kvtnode.key)+','+str(kvtnode.value)+')'
                after = in_order_prim(kvtnode.right)
                return before + this + after

        return in_order_prim(self.__root)


