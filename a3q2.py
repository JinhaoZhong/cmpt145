##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

def create():
    """
    Purpose:
        Create a Statistics record.
    Pre-conditions:
        (none)
    Post-conditions:
        a new record is allocated
    Return:
        A reference to a Statistics record.
    """
    b = {}
    b['count'] = 0      # how many data values have been seen
    b['avg'] = 0        # the running average so far

    b['max'] = None
    b['min'] = None
    return b


def add(stat, value):
    """
    Purpose:
        Use the given value in the calculation of statistics.
    Pre-Conditions:
        stat: a Statistics record
        value: the value to be added
    Post-Conditions:
        none
    Return:
        none
    """
    stat['count'] += 1
    k = stat['count']           # convenience
    diff = value - stat['avg']  # convenience
    stat['avg'] += diff/k



    ##max and min
    if stat['max'] is None:
        stat['max'] = value
        stat['min'] = value
    else:
        stat['min'] = min(value, stat['min'])
        stat['max'] = max(value, stat['max'])

def mean(stat):
    """
    Purpose:
        Return the mean of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The mean of the data seen so far.
        Note: if no data has been seen, 0 is returned.
              This is clearly false.
    """
    return stat['avg']

def count(stat):
    """
    Purpose:
        Return the the number or all the value.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        How many numbers are there in the stat
    """
    return stat['count']

def maximum(stat):
    """
    Purpose:
        Return the maximum value .
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The maximum value that could find
    """
    return stat['max']

def minimum(stat):
    """
    Purpose:
        Return the minimum value
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The minimum value that could find
    """
    return stat['min']