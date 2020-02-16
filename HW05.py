#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW05 - Advanced Lists, Tuples, and Modules
"""
import math
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



def wasted_food(food):
    per = 0.0
    least = 100.0
    j = 0
    equalcheck = 0
    for i in range(1,len(food)):
        per = (100* food[i][1]) / food[i][0]
        per = round(per,2)
        if least > per :
            least = per
            j = i
            equalcheck = food[i][1]

        if least == per and equalcheck > food[i][1]:
            least = per
            j = i
            equalcheck = food[i][1]

            
    tuple = (food[0][j-1], least)    
    return tuple  
        

"""
Function name: ancestors()
Parameters: names (list), surname (str)
Returns: list
"""
def ancestors(a,b):
    j = []
    ans = []
    for i in a:
        j.append(i.split())

    for k in range(0,len(j)):
        if j[k][1] == b and len(j[k]) == 2:

            
            ans.append(j[k][0])

    return ans



"""
Function name: trigonometry
Parameters: degree (str), operation (str)
Returns: float
"""

def trignometry(a,b):
    deg = float(a)

    rad = math.radians(deg)

    if b == "cosine":
        return math.cosine(rad)

     if b == "sine":
        return math.sine(rad)
    
     if b == "tangent":
        return math.tangent(rad)

     else:
         return rad
    
    

    


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


