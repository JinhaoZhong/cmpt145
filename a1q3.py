##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05

N= int(input('how many row do you want:'))
num= str(input('enter your triangle:'))

##create a correct pascal triangle in the list
list=[]
for x in range(N):
    list.append([])
    for y in range (x+1):
        list[x].append(0)
        if y==0 or x==y:
            list[x][y]=1
        else:
            list[x][y]=list[x-1][y-1]+list[x-1][y]

##make the number you enter into triangle and check if it the same
##as the corret one
check_list=[]



if check_list==list:
    print('yes')
else:
    print('no')
print(check_list)




