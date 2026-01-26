# WA Function to check string is palindrome or not ?
def palindrome(a):
    if a.lower() == a.lower()[::-1]:
        return 'Palindome'
    else:
        return 'Not  a palindrome'
    
print(palindrome('mom')) #palindrome
print(palindrome('red')) #not a palindrome

 


#WA function to check  palindrome in a list ?

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


