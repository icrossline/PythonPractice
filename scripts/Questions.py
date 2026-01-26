
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
#=================WAP to find largest number in a given list=====================
#================================================================================

num=[1,5,2,8,6,9,3]
largest=num[0]
index=0

for n in  range(len(num)):
    if largest<num[n]:
        largest=num[n]
        index=n
        
        
print(f"The greatest number in given list is {largest} present at index no.{index}")  #The greatest number in given list is 9 present at index no.5  


#================================================================================
#======WAP to find a second largest and second element in a given list===========
#================================================================================

num=[1,5,2,6,9,3]
largest=num[0]
secondLargest=num[1]

for n in num:
    if largest<n:
        secondLargest = largest
        largest= n
    
print(f'{largest} is the largest.\n{secondLargest} is the second largest element in a given List') #9 is the largest.
                                                                                                   #6 is the second largest element in a given List


#================================================================================
#======WAP to find list is sorted or not ===========
#================================================================================

lst=[1,3,4,8,5,4]

for n in range(len(lst)):
    if lst[n]<lst[n+1]:
        continue
    else:
        print('Your list is not sorted')
        break
else:
    print('Your list is sorted')



