#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW05 - Advanced Lists, Tuples, and Modules
"""

"""
Function name: summer_job()
Parameters: jobs (list of tuples)
Returns: string
"""

def summer_job(a):
    pay = 0
    final = 0
    ans = ""
    
    for i in a:
        pay= i[1] * i[2] 
        if pay > final :
            final = pay
            ans = i[0]

    return ans

            


"""
Function name: wasted_food()
Parameters: meals (list of list and tuples)
Returns: tuple
"""

foods= [["pizza","sand"],(1,2),(2,3)]

def wasted_food(food):
    per = 0.0
    least = 100.0
    j = 0
    for i in range(1,len(food)+1):
        per = (100* food[i][1]) // food[i][0]
        if least > per :
            least = per
            j = i

            
    tuple = (food[0][j-1], least)    
    return tuple  
        
        

"""
Function name: ancestors()
Parameters: names (list), surname (str)
Returns: list
"""
def ancestors(a,b):

    return 0



"""
Function name: trigonometry
Parameters: degree (str), operation (str)
Returns: float
"""

def trignometry(a,b):
    return 0


"""
Function name: days_of_the_week()
Parameters: birthdays (list of tuples), year (int)
Returns: list
"""
def days_of_the_week(a,b):
    return 0

"""
Function name: donation_amount()
Parameters: donations (list of strs)
Returns: float
"""
def donation_amount(a):
    return 0


