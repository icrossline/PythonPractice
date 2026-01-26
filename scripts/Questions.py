
#================================================================================
#============= WA Function to check string is palindrome or not ?================
#================================================================================
def palindrome(a):
    if a.lower() == a.lower()[::-1]:
        return 'Palindome'
    else:
        return 'Not  a palindrome'
    
print(palindrome('mom')) #palindrome
print(palindrome('red')) #not a palindrome

 

#================================================================================
#=================WA function to check  palindrome in a list ?===================
#================================================================================

def palindromelist(a):
    for ch in a:
        if ch.lower() == ch.lower()[::-1]:
            res.append(ch)
        else:
            pass
    return res    
    
res=[] #Empty list       

palindromelist(['mom','red','racecar']) 
print(res) #return mom and racecar

#================================================================================
#=================WAP to find largest number in a given list with a index=====================
#================================================================================

num=[1,5,2,8,6,9,3]
largest=num[0]
index=0

for n in  range(len(num)):
    if largest < num[n]:
        largest=num[n]
        index=n
        
        
print(f"The greatest number in given list is {largest} present at index no.{index}")  #The greatest number in given list is 9 present at index no.5  


#================================================================================
#======WAP to find a second largest and second element in a given list===========
#================================================================================

lst=[10,221,11,8,4]

def sorted_lst(lst):
    largest=lst[0]
    second=lst[0]
    for curr  in lst:
        if curr > largest:
            second =largest
            largest=curr
        elif curr < largest and curr > second:
            second=curr
    return second

print(sorted_lst(lst))    
#================================================================================
#======WAP to find list is sorted or not ===========
#================================================================================

lst=[1,3,4,8,5,4]

for n in range(len(lst)-1):
    if lst[n]<lst[n+1]:
        continue
    else:
        print('Your list is not sorted')
        break
else:
    print('Your list is sorted')

#================================================================================
#======WAP to find duplicate element in a list ===========
#================================================================================

lst=[1,2,2,3,3,5,4,5]
newList=[]
duplicate=[]
for  i in lst:
    if i in newList:
        duplicate.append(i)
    else:
        newList.append(i)

print(f'{duplicate} are the duplicates in the given List')


