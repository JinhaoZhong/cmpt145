##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 class:Cmpt145  L05

import a2q1 as checker
import sys as sys

thewordtotest = "JAYWALKING"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("Error: the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = "BADSINGING"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("Error: the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = "REDRUM"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = "BEINGSMELLY"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = "SMOKING"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = "SCAMS"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is not in the matrix")

thewordtotest = "CONNING"
result = checker.check(thewordtotest, checker.make_list(checker.read_file("confession.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is not in the matrix")

print('***************************confession.txt checked*********************************')

thewordtotest = 'HMM'
result = checker.check(thewordtotest, checker.make_list(checker.read_file("test_file.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is in the matrix")

thewordtotest = 'EUREKA'
result = checker.check(thewordtotest, checker.make_list(checker.read_file("test_file.txt")))
if (result != 'YES'):
    print("the word to be tested ", thewordtotest, " is in the matrix")

print('*****************************tset_file.txt checked*******************************')

