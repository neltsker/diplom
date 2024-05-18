from .schemas import *
import re
class Uservalidator():
    def validate(self,User):
        pass
    
    
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def UserValidator(user):
    if user.firstName == '' or user.firstName == None or user.firstName.isspace():
        return False
    if user.lastName == '' or user.lastName == None or user.lastName.isspace():
        return False
    if user.password == '' or user.password == None or user.password.isspace():
        return False
    if(re.fullmatch(regex, user.email)):
        return True
        print("Valid Email")
 
    else:
        return False
        print("Invalid Email")