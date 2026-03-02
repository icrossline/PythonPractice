#decorator let you add a addtional behaviour to the function


#Build a authentication system using decorator
from functools import wraps # wraps preserve the metadata 
def decorator(func): #Decorator function
  def wrapper(user_role):
    if user_role.lower() !='admin':
      print("Access Denied ")
    else:
      return func(user_role)
  return wrapper

role="admin" #give access if role is admin 
@decorator # What ever func you write after this it will directly go to the decorator
def user(role):
  print("Access Granted")

user(role)
  
  
    
