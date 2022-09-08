##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import a8q1 as a8q1
import exampletrees as example
import treenode as tn

eg1 = example.atree
eg2 = example.mtree
eg3 = example.ctree
eg4 = example.xtree
eg5 = example.fibonatree
eg6 = example.expr_tree

###########################################################################

test_count_node_types=[
    {'inputs' : eg1,
     'outputs' :({'data': 11, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None}, {'data': 5, 'left': None, 'right': None}) ,
     'reason': 'atree checked'},

    {'inputs' : eg2,
     'outputs' : None,
     'reason': 'mtree checked'},

    {'inputs': eg3,
     'outputs': ({'data': 11, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None}, {'data': 5, 'left': None, 'right': None},
                 {'data': 'si', 'left': None, 'right': None}),
     'reason': 'ctree checked'},

    {'inputs': eg4,
     'outputs': ({'data': 11, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None}, {'data': 5, 'left': None, 'right': None},
                 {'data': 'si', 'left': None, 'right': None}, {'data': 2, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None},
                 {'data': 3, 'left': None, 'right': None}, {'data': 3, 'left': None, 'right': None}),
     'reason': 'xtree checked'},

    {'inputs': eg5,
     'outputs': ({'data': 11, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None}, {'data': 5, 'left': None, 'right': None},
                 {'data': 'si', 'left': None, 'right': None}, {'data': 2, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None},
                 {'data': 3, 'left': None, 'right': None}, {'data': 3, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None},
                 {'data': 0, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None}, {'data': 0, 'left': None, 'right': None}, {
                     'data': 1, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None}, {'data': 0, 'left': None, 'right': None},
                 {'data': 1, 'left': None, 'right': None}),
     'reason': 'fibonatree checked'},

    {'inputs': eg6,
     'outputs':({'data': 11, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None}, {'data': 5, 'left': None, 'right': None},
                {'data': 'si', 'left': None, 'right': None}, {'data': 2, 'left': None, 'right': None}, {'data': 6, 'left': None, 'right': None},
                {'data': 3, 'left': None, 'right': None}, {'data': 3, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None},
                {'data': 0, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None}, {'data': 0, 'left': None, 'right': None},
                {'data': 1, 'left': None, 'right': None}, {'data': 1, 'left': None, 'right': None}, {'data': 0, 'left': None, 'right': None},
                {'data': 1, 'left': None, 'right': None}, {'data': 2.0, 'left': None, 'right': None}, {'data': 3.0, 'left': None, 'right': None},
                {'data': 3.0, 'left': None, 'right': None}, {'data': 4.0, 'left': None, 'right': None}, {'data': 2.0, 'left': None, 'right': None},
                {'data': 89.0, 'left': None, 'right': None}, {'data': 3.0, 'left': None, 'right': None}),
     'reason': 'expr_tree checked'},
]

for t in test_count_node_types:
    tnode = t['inputs']
    result = a8q1.count_node_types(tnode)
    expected = t['outputs']
    if result != expected:
        print('Error in count_node_types: expected ', expected, 'but got', result, '---', t['reason'])

##########################################################################
test_copy=[
    {'inputs' : eg1,
     'outputs' : eg1,
     'reason': 'atree checked'},

    {'inputs' : eg2,
     'outputs' : eg2,
     'reason': 'mtree checked'},

    {'inputs': eg3,
     'outputs': eg3,
     'reason': 'ctree checked'},

    {'inputs': eg4,
     'outputs': eg4,
     'reason': 'xtree checked'},

    {'inputs': eg5,
     'outputs': eg5,
     'reason': 'fibonatree checked'},

    {'inputs': eg6,
     'outputs': eg6,
     'reason': 'expr_tree checked'},
]


for t in test_copy:
    tnode = t['inputs']
    result = a8q1.copy(tnode)
    expected = t['outputs']
    if result != expected:
        print('Error in copy(): expected ', expected, 'but got', result, '---', t['reason'])


print('**************************************test complete*****************************************')




