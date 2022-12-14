# CMPT 145: Huffman Codes
# Defines the Huffman Tree data structure
#
# A Huffman tree-node has a character and a frequency.


# some strings to avoid long lines later
_INIT_ASSERT_MESSAGE_NONLEAF  = 'Invalid Huffman tree construction attempted.'
_GETCH_ASSERT_MESSAGE_NONLEAF = 'Method get_char() called on non-leaf node'


class HuffmanTree(object):

    def __init__(self, freq=0, char=None, left=None, right=None):
        """
        Purpose:
            Initializes the HuffmanTree object.
            To create a leaf node
                aleaf = HuffmanTree(freq=10, char='A')
                bleaf = HuffmanTree(freq=15, char='E')
            To create an internal node:
                node = HuffmanTree(left=aleaf,right=bleaf)

        Pre-conditions:
            :param freq: a positive integer
            :param char: a character
            :param left: another Huffman Tree
            :param right: another HuffmanTree
        """
        self.__char = char
        self.left = left
        self.right = right

        if left is None and right is None:
            # leaf node: assign the frequency as given
            self.__freq = freq
        else:
            assert left is not None and right is not None, _INIT_ASSERT_MESSAGE_NONLEAF
            # non-leaf node: calculate the frequency from the given subtrees
            self.__freq = left.__freq + right.__freq

    def is_leaf(self):
        """
        Purpose: 
            Check if the node is a leaf.
            Simplifies some of the other methods with an abstraction.
        Return: 
            True if the node is a leaf node
        """
        return self.left is None and self.right is None

    def get_freq(self):
        """
        Purpose:
            Return the frequency data stored in the node.
        Return:
            :return: the frequency
        """
        return self.__freq

    def get_char(self):
        """
        Purpose:
            Return the character stored at a leaf node.
        Return:
            :return: the character at a leaf node
        """
        assert self.is_leaf(), _GETCH_ASSERT_MESSAGE_NONLEAF
        return self.__char

    def display(self, level=0):
        """
        Purpose:
            For debugging, display the tree.
            The structure of the tree is represented by indentation
            No other real purpose.
        Preconditions:
            :param level: indentation amount for subtrees.
        Return
            :return: None
        """
        if self.is_leaf():
            print(' '*level+'Leaf:', self.__char, self.__freq)
        else:
            print(' '*level+'Node:', self.__freq, 'Children:')
            self.left.display(level+1)
            self.right.display(level+1)

    def build_codec(self):
        """
        Purpose:
            Build a dictionary of char-code pairs from the Huffman tree.
        Return:
            :return: a dictionary with character as key, code as value
        """
        codes = {}
        def encoder(tree, code):
            if tree.is_leaf():
                codes[tree.get_char()] = code
            else:
                encoder(tree.left, code+'0')
                encoder(tree.right, code+'1')

        if self.is_leaf():
            codes[self.__char] = '0'
        else:
            encoder(self,'')
        return codes

    def __lt__(self, other):
        return self.__freq < other.__freq

    def __str__(self):
        if self.is_leaf():
            return str(1)+self.__char
        else:
            return str(0) + str(self.left) + str(self.right)

