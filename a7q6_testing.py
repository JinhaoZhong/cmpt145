##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import node as node
import a7q6 as a7q6


test_average=[
    {'inputs' : None,
     'outputs' : None,
     'reason': 'empty chain'},

    {'inputs' : [6],
     'outputs' : [6],
     'reason' : 'A chain with one node'},

    {'inputs' : [1,2,3],
     'outputs' : [2],
     'reason' : 'Achain with several nodes'},

    {'inputs': [0.8, 2.1, 3.1],
     'outputs': [2],
     'reason': 'A chain has floats'},

    {'inputs' : [1, 2.8, 2.2],
     'outputs' : [2],
     'reason': 'A chain has float and integer'},

    {'inputs' : [-1,-2,-3],
     'outputs' : [-2],
     'reason' : 'A chain negative integer'},

    {'inputs' : [-0.8, -2.1, -3.1],
     'outputs' : [-2],
     'reason' : 'A chain with negative floats'},

    {'inputs' : [-1, -2.8, -2.2],
     'outputs' : [-2],
     'reason': 'A chain has negative float and integer'},

    {'inputs' : [-6, -2, 6, 10],
     'outputs' : [2],
     'reason': 'A chain has positive and negative float and integer'}
]


##for t in test_average:
 #   chain= t['inputs']
 #   expected = t['outputs']
 #   result =  a7q6.average(chain, count=0, sum=0)
 #   if result!= expected:
 #       print('Error in average, expected', expected, 'but got', 'result', '----',t['reason'] )

###########################################################################################################

test_reverse = [
    {'inputs' : None,
     'outputs' : None,
     'reason': 'empty chain'},

    {'inputs' :  node.create('6', None),
     'outputs' : node.create('6', None),
     'reason': 'A chain with one node'},

    {'inputs' :  node.create('1',node.create('2',node.create('3'))),
     'outputs' : node.create('3',node.create('2',node.create('1'))),
     'reason': 'A chain with several nodes'},
]


for t in test_reverse:
    chain = t['inputs']
    result = a7q6.reverse(chain)
    expected = t['outputs']
    if result != expected:
        print('Error in reverse(): expected ', expected, 'but got', result, '---', t['reason'])


#########################################################################################################

test_copy = [
    {'inputs' : None,
     'outputs' : None,
     'reason': 'A empty chain'},

    {'inputs' :  node.create('66', None),
     'outputs' : None,
     'reason': 'A chain with one node'},

    {'inputs' :  node.create('1',node.create('2',node.create('3'))),
     'outputs' : None,
     'reason': 'A chain with several nodes'},
]

for t in test_copy:
    chain = t['inputs']
    result = a7q6.copy(chain)
    if chain is None and result is not None:
        print('Error in copy(): expected ', None, 'but got', None, '---', t['reason'])
    elif chain is not None:
        if chain != result:
            print('Error in copy: expected a same chain', '---', t['reason'])
        if chain is result:
            print('Error in copy: expected different chain', '---', t['reason'])


print('****** test complete ******')