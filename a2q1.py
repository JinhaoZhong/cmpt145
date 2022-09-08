##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 class:Cmpt145  L05
import sys as sys


def read_file(file_name):
    ##list is all the str in txt file
    list = []
    ##input the file name in terminal to open it

    ##open the file and append the data into list
    f = open(file_name).readlines()
    for line in f:
        list.append(line)
    list=''.join(list).replace('\r\n', ' ')
    return list

def make_list(list):
    ## n is the number for adding str into columns
    ##row is the list for rows in txt file
    ##col is the list for columns in txt file
    n=0
    row=[]
    col=[]



    ##append data into row list
    row.append(list)
    row = ''.join(row).replace(' ', '')

    ##append data into columns list
    while n < 14:
        col.append(list[n::15])
        n = n + 1
    col = ''.join(col).replace(' ', '')

    ##reverse the row list and turn into rev_row
    rev_row = row[::-1]

    ##reverse the columns list and turn into rev_col
    rev_col = col[::-1]

    ##add all the list together, a big_list that contain all the data
    big_list = row + col + rev_row + rev_col
    return big_list




def check(N, big_list):
    ##check if the word in the txt file
    result = ''
    if N in big_list:
        result = 'YES'
    else:
        result = 'NO'
    return result
if  __name__ == '__main__':
    file = sys.argv[1]
    ##iput the words in terminal to find it
    N = sys.argv[2]

    list = read_file(file)
    print(check(N,make_list(list)))

