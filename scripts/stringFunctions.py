str='Hello WOrld'


#Modify/Replace 
print(str.replace('WOrld','World'))  #Replace Value 
print(str.split()) str  to list #convert string to list
print(' '.join(['Hello','World'])) list to str #convert list to string


# Case Conversion Functions
 print(str.upper()) #Convert into UPPER CASE
 print(str.lower()) #Convert into lower case
 print(str.capitalize())  #Capitalize First Letter of entire string 
 print(str.title()) #Capitalize First Letter of every word in a string 
 print(str.swapcase()) #COnvert lower To UPPER and UPPER to lower case

#Remove Spaces
 print(str.strip()) # Remove space from Both Side
 print(str.rstrip()) #Remove space from right side 
 print(str.lstrip()) #Remove Space from Left Side

#Search / Count
 print(str.find('a')) #Return index , -1 if not found also find first occurrence
 print(str.rfind('a')) # find Last occurrence
 print(str.count('e')) # Count no. of occurrence
 print(str.index('e')) # Return index , value Error if not found
 print(str.startswith('H')) #Return True if start with else False
 print(str.endswith('e')) # Return True if ends with ekse False

#Alignment
str='12'

print(str.ljust(6,'*')) #align left
print(str.rjust(6,"*")) #align right
print(str.center(6,'*')) # align center
