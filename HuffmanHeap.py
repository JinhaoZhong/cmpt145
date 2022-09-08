# CMPT 145: Huffman Codes
# Defines a data structure that allows Huffman codes to
# be computed efficiently.
#
# A Huffman Heap is a queue to store HuffmanTree objects.
# The word "heap" implies that the dequeue operation will always 
# remove and return the HuffmanTree object with the lowest frequency.


class HuffmanHeap(object):
    def __init__(self, leafs):
        """
        Purpose:
            Creates a new HuffmanHeap object.
        Pre-conditions:
            leafs: a list of HuffmanTree leaf nodes.
        Post-conditions:
            The heap is created and initialized.
        Return:
            None
        """
        self.__leafs = leafs
        self.__list = []

    def enqueue(self, tree):
        """
        Purpose:
            Adds the tree to the Heap.  
            This is an O(1) operation.
        Pre-conditions:
            tree is a HuffmanTree object
        Post-conditions:
            the heap increases in size by 1
        Return:
            None
        """
        self.__list.append(tree)

    def dequeue(self):
        """
        Purpose:
            Return the smallest value in the queue.
            This is an O(1) operation.
        Pre-conditions:
            None
        Post-conditions:
            The heap decreases in size by 1
        Return:
            A HuffmanTree object, with the lowest frequency
        """
        if len(self.__leafs) == 0:
            return self.__list.pop(0)
        elif len(self.__list) == 0:
            return self.__leafs.pop(0)

        elif self.__leafs[0] > self.__list[0]:
            return self.__list.pop(0)
        else:
            return self.__leafs.pop(0)

    def __len__(self):
        """
        Purpose:
            Return the number of data values stored in the heap.
            This method allows Python scripts to call len(hh)
            if hh is a HuffmanHeap object.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            The number of values stored in the heap
        """
        return len(self.__leafs)+len(self.__list)

    def display(self):
        """
        Purpose:
            Display the data for debugging.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            None
        """


        print('leafs:', self.__leafs)
        print('list:  ', self.__list)


if __name__ == '__main__':
    test= HuffmanHeap([1,2,3,4,5,6,6,7,8,9,10])
    test.display()
    while len(test)!=1:
        output = test.dequeue()
        output1 = test.dequeue()
        test.enqueue(output+ output1)
        test.display()
    print('******test complete******')