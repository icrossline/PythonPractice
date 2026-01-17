#Q1   Print the square pattern. 

      * * * * * 
      * * * * * 
      * * * * * 
      * * * * * 
      * * * * *   


Sol:
    n=5 #its represent the number how many times you want to print rows/columns
    for rows in range(1,n+1): #run for rows 
      for col in range(1,n+1): # run for columns
        print('*',end=' ')  # print'*' until it reaches to n+1 than end= ' ' break the line after completingthe nested loop
      print() # adds a new line

      i=1 # row 1
      j=1 to n+1 =>  * * * * *  #col run 1 to 5
      i=2 # row =2
      j=1 to n+1 =>  * * * * *  # col run 1 To 5
      i=3 #row=3
      j=1 to n+1 =>  * * * * *  .. # col run 1 to 5 and so on.


#Q2  Increasing Triangle Pattern
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
#sol-
       n=5

      for row in range(1,n+1): #run for 5 rows
          for col in range(1,row+1): # run for 5 column
              print('*',end=" ") 
          print()
    i=1                   
      j=i+1 =>  * 
    i=2
       j=i+2 => * * 
    i=3
        j=i+3=> * * *   #...it will run till the iteration got complete.

  #Q3 Decreasing triangle pattern

        * * * * * 
        * * * * 
        * * * 
        * * 
        * 

#Sol. 
  n=5
=>  i=1 
  j=i,n+1 # * * * * *  
=>  i=2
  j=i,n+1 # * * * * 
=>  i=3
  j=i,n+1 # * * * 
=>  i=4
  j=i,n+1 # * * 
 => i=5
  j=i,n+1 # * 


CODE:-
n=5
for row in range(1,n+1):
    for col in range(row,n+1):
        print('*',end=' ')
    print()




      

