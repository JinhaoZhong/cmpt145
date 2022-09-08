##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

import treenode as tn

def bad_complete(tnode):
    def cmplt ( tnode ):
        if tnode is None :
            return True, 0
        else :
            lflag, ldepth = cmplt(tn.get_left(tnode))
            if not lflag:
                return False, None
            rflag, rdepth = cmplt(tn.get_right(tnode))
            if not rflag:
                return False, None
            elif ldepth == rdepth :
                return True, ldepth + 1
            else:
                return False, None
    result = cmplt(tnode)
    return result

