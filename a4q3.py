##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05


print('Welcome to PARENTHESIS CHECKER 9000, Let"s BRACKET !')

import a4q2 as check

expression=[]

result = check.if_balance(expression)

while result is True:
    expression = input('enter:')
    print('is balance')

else:
    print('Is and unbalanced expression')