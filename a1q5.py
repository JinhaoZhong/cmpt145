##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05
def get_data(n, data):
    data = []
    for i in range(n):
        data.append(input('Enter one integer only:'))
    return data

def find_min_and_max(data, the_min, the_max):
    the_min = min(data)
    the_max = max(data)

def counting(data):
    the_min = min(data)
    the_max = max(data)
    find_min_and_max(data, the_min, the_max)

    fsize=int(the_max)+1
    frequency=[0]*fsize
    mini=int(the_min)
    while (mini<int(the_max)+1):
        frequency[mini]=0
        mini+=1
    for d in data:
        frequency[int(d)]+=1
    return frequency

def draw_histogram(frequency, the_min, the_max):
    print("\n\n\n ----------- Histogram ----------------\n")

    for f in frequency:
        print(f, '*'*f)

data_size = int(input('How many data values?'))
data = get_data(data_size, [])
frequency = counting(data)
for i in range(len(frequency)):
    if frequency[i]!=0:
        print(i,end='')
    for i in range (frequency[i]):
        print('*',end='')



