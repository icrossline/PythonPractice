n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
print()



for i in range(1,n+1):
    for k in range(1,i):
        print('-',end=' ')
    for j in range(n-i+1):
        print('*',end=' ')
    print()   
print()


for i in range(1,n+1):
    for j in range(n-i+1):
        print('*',end=' ')
    print()   
print()

for i in range(1,n+1):
    for j in range(n-i):
        print('-',end=' ')
    for k in range(1,i+1):
        print('*',end=' ') 
    print()   
print()


for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end=' ')
    print()        
for i in range(2,n+1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(n-i+1):
        print('*',end=' ')
    print()  

print()

for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(n-i+1):
        print('*',end=' ')
    print()  
for i in range(2,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end=' ')
    print()         


print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()
print()     



for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==4 or j==4):
            print('*',end=' ')       
        else:
            print(' ',end=' ') 
    print()          
     
print()   

for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1 ):
            print('*',end=' ')       
        else:
            print(' ',end=' ') 
    print()          
     
print()   

for i in range(n):
    for j in range(i+1):
        if i==j or j==0 or i==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')    
    print()

print()

for i in range(n):
    for j in range(n-i):
        if i + j == n-1 or i==0 or j==0:
            print('*',end=' ')
        else:
            print(' ' , end=' ')       
    print()

print()


for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(1,n-i+2):
        if i == 1 or k == 1 or k == n - i + 1:
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()

print()



