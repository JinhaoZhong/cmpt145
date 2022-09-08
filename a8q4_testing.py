##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import treenode as tn
import a8q4 as a8q4
import math as math


tnc = tn.create
test_ordered = [
    {'inputs': None,
     'outputs': True,
     'reason': 'Empty tree'},

    {'inputs': tnc(6),
     'outputs': True,
     'reason': 'A tree with no child'},

    {'inputs': tnc(6, tnc(2)),
     'outputs': True,
     'reason': 'An order tree with only left child'},

    {'inputs': tnc(3, None, tnc(6)),
     'outputs': True,
     'reason': 'An order tree with only right child'},

    {'inputs': tnc(3, tnc(2), tnc(6)),
     'outputs': True,
     'reason': 'An ordered tree'},

    {'inputs': tnc(6, tnc(3, tnc(2), tnc(5)), tnc(8, tnc(7), tnc(16))),
     'outputs': True,
     'reason': 'A larger ordered tree'},

    {'inputs': tnc(6, tnc(3, tnc(2), None), tnc(8, tnc(7), tnc(16))),
     'outputs': True,
     'reason': 'A ordered tree with uncomplete left child'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(6), None)),
     'outputs': True,
     'reason': 'A ordered tree with uncomplete right child'},

    {'inputs': tnc(6, tnc(9)),
     'outputs': False,
     'reason': 'A tree with large left child'},

    {'inputs': tnc(6, None, tnc(3)),
     'outputs': False,
     'reason': 'A tree with small right child and no left child'},

    {'inputs': tnc(6, tnc(2), tnc(3)),
     'outputs': False,
     'reason': 'A tree with small right child'},

    {'inputs': tnc(6, tnc(2, tnc(5), tnc(3)), tnc(7, tnc(6), tnc(10))),
     'outputs': False,
     'reason': 'An tree with unordered on left side 1'},

    {'inputs': tnc(6, tnc(2, tnc(1), tnc(0)), tnc(9, tnc(8), tnc(10))),
     'outputs': False,
     'reason': 'An tree with unordered on left side 2'},

    {'inputs': tnc(6, tnc(3, tnc(1), tnc(5)), tnc(9, tnc(0), tnc(10))),
     'outputs': False,
     'reason': 'An tree with unordered on right side 1'},

    {'inputs': tnc(6, tnc(2, tnc(1), tnc(3)), tnc(9, tnc(6), tnc(3))),
     'outputs': False,
     'reason': 'An tree with unordered on right side 2'}
]

for t in test_ordered:
    tree = t['inputs']
    expected = t['outputs']
    assert a8q4.ordered(tree) is expected, t['reason']

print('**************test complete*****************')
