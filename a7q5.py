##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

def Fib_seq(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib_seq(n-1)+ Fib_seq(n-2)


def Moos_seq(n):
    if n == 0:
        print('0')
    elif n == 1:
        return 1
    elif n ==2:
        return 2
    else:
        return Moos_seq(n-1) + Moos_seq(n-2) + Moos_seq(n-3)


def substr(s, c, r):
    if s == '':
        return s
    else:
        target = s[0]
        if s[0] == c:
            target = r
        return target + substr(s[1:], c, r)

