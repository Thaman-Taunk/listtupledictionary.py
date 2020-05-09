#assigning elements to different lists
l1=[]
l2=[]
n1=int(input("size of l1"))
n2=int(input("size of l2"))
i=0
print('enter elements of list1')
while i<n1:
    l1.append(input())
    i+=1
print('list1 elements are...')
print(l1)
print('enter elements of list2')
i=0
while i<n2:
    l2.append(input())
    i+=1
print('list2 elements are...')
print(l2)    
#accessing elements from a tuple
tup=(1,2,3,4,5)
print(tup)
print('different elements of tuple are....')
i=0
while i<len(tup):
    print(tup[i])
    i+=1
#deleting different dictionary elements
mydict={'1':'ab','2':'cd','3':'ef','4':'gh'}
print(mydict)
del mydict['1']
del mydict['3']
print('after deleting elements...')
print(mydict)
