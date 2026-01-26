# WA Function to check string is palindrome or not ?
def palindrome(a):
    if a.lower() == a.lower()[::-1]:
        return True
    else:
        return False
    
if palindrome('racecar'):
    print('Palindrome')
else:
    print('Not a palindrome')


#WA function to check  palindrome in a list ?

def palindromelist(a):
    for ch in a:
        if ch == ch[::-1]:
            res.append(ch)
        else:
            pass
    return res    
    
res=[]        

palindromelist(['mom','red','racecar']) 
print(res)


