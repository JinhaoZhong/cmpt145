# Assignment 3: ADTs and Testing

# This script is a starter file for testing the Statistics ADT

import a3q2 as Stat

#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # we'll open the data structure in these tests
    # check the initial count
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0], # [count, avg]
     'reason' : 'No change to avg'},

    {'inputs' : [6],
     'outputs' : [1, 6],
     'reason' : 'A positive value.'},

    {'inputs' : [-6],
     'outputs' : [1, -6],
     'reason' : 'A negative value.'},

    {'inputs' : [6.6],
     'outputs' : [1, 6.6],
     'reason' : 'A positive floating point value'},

    {'inputs' : [-6.6],
     'outputs' : [1, -6.6],
     'reason' : 'A negative floating point value'}
]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # now call add()
    Stat.add(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5, 0],          #[count, avg]
     'reason' : 'All zeroes'},

    {'inputs' : [3,6,9],
     'outputs':[3, 6],
     'reason' : 'All positive value'},

    {'inputs' : [-3,-6,-9],
     'outputs':[3, -6],
     'reason' : 'All negative value'},

    {'inputs' : [-6,0,6],
     'outputs':[3, 0],
     'reason' : 'Positive and negative value'},

    {'inputs' : [-3,0,6],
     'outputs':[3, 1],
     'reason' : 'Positive and negative value'},

    {'inputs' : [3.3, 6.6, 9.9],
     'outputs':[3, 6.6],
     'reason' : 'Positive floats'},

    {'inputs' : [-3.3, -6.6, -9.9],
     'outputs':[3, -6.6],
     'reason' : 'Negative floats'},

    {'inputs' : [-1.1, -0.9, 2.5, 1.5],
     'outputs':[4, 0.5],
     'reason' : 'Positive floats and negative floats'},

    {'inputs' : [-6, -1.5, 1.5, 2],
     'outputs':[4, -1],
     'reason' : 'Positive and negative floats and integer'}

]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call mean()
    result = Stat.mean(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

    # check the result of mean()
    if result != expected[1]:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])


#######################################################
#test statistic count

tets_count= [
    {'inputs' : [],
     'outputs':[],
     'reason' : 'No value count'},

    {'inputs' : [6],
     'outputs':[1],
     'reason' : 'Single value count'},

    {'inputs' : [1,2,3,4,5,6],
     'outputs':[6],
     'reason' : 'Positive value count'},

    {'inputs' : [-1,-2,-3,-4,-5,-6],
     'outputs':[6],
     'reason' : 'Negative value count'},

    {'inputs' : [6,66,666],
     'outputs':[3],
     'reason' : 'Value count which is odd'},

    {'inputs' : [6,66],
     'outputs':[2],
     'reason' : 'Value count which is even'}
]

if thing['count'] != expected[0]:
    print('Error in add(): expected count', expected[0],
          ' but found ', thing['count'], '--', t['reason'])

######################################################
##test statistic max

test_max=[
    {'inputs' : [],
     'outputs':[None],
     'reason' : 'No input'},

    {'inputs' : [6,6,6,6,6,6,6],
     'outputs':[6],
     'reason' : 'All same positive integer'},

    {'inputs' : [-6,-6,-6,],
     'outputs':[-6],
     'reason' : 'All same negative integer'},

    {'inputs' : [6,66,666],
     'outputs':[666],
     'reason' : 'All positive integer'},

    {'inputs' : [-666, -66, -6],
     'outputs':[-6],
     'reason' : 'All negative integer'},

    {'inputs' : [-66,-6,0,6,66],
     'outputs':[66],
     'reason' : 'Both negative and positive integer and zero'},

    {'inputs' : [6.6, 66.6, 666.6],
     'outputs':[666.6],
     'reason' : 'All positive float'},

    {'inputs' : [-666.6, -66.6, -6.6],
     'outputs':[-6.6],
     'reason' : 'All negative float'},

    {'inputs' : [-66.6, -6.6, 6.6, 66.6],
     'outputs':[66.6],
     'reason' : 'Both negative and positive float'},

    {'inputs' : [-66.6, -6.6, -6, 6.6, 66.6, 666],
     'outputs':[666],
     'reason' : 'Both negative and positive float and integer'}
]

for t in test_max:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call maximum()
    result = Stat.maximum(thing)

    # check max
    if result != expected[0]:
        print('Error in maximum(): expected maximum', expected[0],
              ' but found ', result, '--', t['reason'])

##################################################################################
##check minimum

test_min=[
    {'inputs' : [],
     'outputs':[None],
     'reason' : 'No input'},

    {'inputs' : [6,6,6,6,6,6,6],
     'outputs':[6],
     'reason' : 'All same positive integer'},

    {'inputs' : [-6,-6,-6,],
     'outputs':[-6],
     'reason' : 'All same negative integer'},

    {'inputs' : [6,66,666],
     'outputs':[6],
     'reason' : 'All positive integer'},

    {'inputs' : [-666, -66, -6],
     'outputs':[-666],
     'reason' : 'All negative integer'},

    {'inputs' : [-66,-6,0,6,66],
     'outputs':[-66],
     'reason' : 'Both negative and positive integer and zero'},

    {'inputs' : [6.6, 66.6, 666.6],
     'outputs':[6.6],
     'reason' : 'All positive float'},

    {'inputs' : [-666.6, -66.6, -6.6],
     'outputs':[-666.6],
     'reason' : 'All negative float'},

    {'inputs' : [-66.6, -6.6, 6.6, 66.6],
     'outputs':[-66.6],
     'reason' : 'Both negative and positive float'},

    {'inputs' : [-66.6, -6.6, -6, 6.6, 66.6, 666],
     'outputs':[-66.6],
     'reason' : 'Both negative and positive float and integer'}
]

for t in test_min:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call maximum()
    result = Stat.minimum(thing)

    # check max
    if result != expected[0]:
        print('Error in minimum(): expected minimum', expected[0],
              ' but found ', result, '--', t['reason'])

########################################################################

print('*** Test script completed ***')