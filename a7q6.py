##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import node as node

def average(chain, count =0, sum = 0 ):
    """
        Purpose
            Find  the average of the chain
        Preconditions:
            :param chain: a node-chain
            :param count: the numbers of value in node chain
            :param sum: the sum of the node chain
        Post-conditions:
            None
        Return:
            :return: the avg of the node chain
        """
    if chain is None:
        if count ==0:
            return 0
        else:
            return sum/count

    else:
        return average(node.get_next(chain), count+1, sum+node.get_data(chain))


def reverse(chain):

    """
    Purpose
        Reverse the sequence of the nodes in the given chain.
    Preconditions:
        :param chain: a node chain
    Post-conditions:
        The values in the chain are in the reversed order.
    Return:
        :return: the reversed node chain
    """

    if chain is None:
        return None
    elif node.get_next(chain) is None:
        return chain
    else:
        prenode = chain
        nextnode = node.get_next(chain)

        reves = reverse(nextnode)

        node.set_next(nextnode, prenode)
        node.set_next(prenode, None)
        return reves


def copy(chain):
    """
        Purpose
            Make a completely new copy of the given node-chain.
        Preconditions:
            :param chain: a node-chain
        Post-conditions:
            None
        Return:
            :return: A new copy of the chain is returned
        """

    if chain is None:
        return None
    else:
        new = node.create(node.get_data(chain) )
        next = copy(node.get_next(chain))
        node.set_next(new, next)
        return new


