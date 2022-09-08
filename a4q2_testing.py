##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05
import a4q2 as check

test=[
## check if all the bracket can be input
    {'inputs':["()"],
     'outputs':[True],
     'reason':'Input parenthesis not correct'},

    {'inputs':["[]"],
    'outputs':[True],
    'reason':'Input square bracket not correct'},

    {'inputs':["{}"],
    'outputs':[True],
    'reason':'Input curly brace not correct'},

##check if there are brackects  can't be matched
    {'inputs':["(()"],
    'outputs':[True],
    'reason':'Left bracket is more than left bracket'},

    {'inputs': ["())"],
    'outputs': [True],
    'reason': 'Left bracket is more than right bracket'},

    {'inputs': ["[]]]"],
     'outputs': [True],
     'reason': 'Right bracket is more than left bracket'},

    {'inputs': ["( ]"],
     'outputs': [True],
     'reason': 'Parenthesis and square bracket does not fit'},

    {'inputs': ["( }"],
     'outputs': [True],
     'reason': 'Parenthesis and curly brace dose not fit'},

    {'inputs': ["[ }"],
     'outputs': [True],
     'reason': 'Square bracket and curly brace does not fit'},
##check if no brackects still right
    {'inputs': [""],
     'outputs': [True],
     'reason': 'No input, not bracket'},

##mixing brackects
    {'inputs': ["([}]"],
     'outputs': [True],
     'reason': 'bracket doest not balance'},

    {'inputs': ["[(  ] )"],
     'outputs': [True],
     'reason': 'Not closing parenthesis before square bracket'},
]

## run the checking
for t in test:
    expression = t['inputs']
    outputs = t['outputs']
    reason = t['reason']
    result = check.if_balance(expression)

## print error if the result is not the same as output
    if len(outputs) != len([result]):
        print('error, ', reason)

print('****************************test complete*****************************')