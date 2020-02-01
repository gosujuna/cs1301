#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing, and Lists
"""

"""
Function name: noteTaker()
Parameters: class (str), courses (list)
Returns: boolean
"""

def noteTaker(s):
    l = list(s)
  
    for i in range(len(l)-2):
        if l[i+2].isupper() or i+2 == len(l):
            if l[i] == '!':
                l[i] = '#'

            if l[i] == '.':
                l[i] = '$'

    if l[-1] == '!':
        l[-1] = '#'

    if l[-1] == '.':
        l[-1] = '$'
                
     
            
                
                
    
    out = "".join(c for c in l if c not in ('!','.',':','@',",","?")
                  )

    
    final = list(out)

    for i in range(len(final)):
        if final[i] == "#":
            final[i] = "!"

        if final[i] == "$":
            final[i] = "."

    done = "".join(final)
        
    return done



"""
Function name: foodDesertLocator()
Parameters: cities (list)
Returns: (list)
"""



def foodDesertLocator(s):
    a= 0
    l= []
    for i in range(0,len(s)):
        if (i) % 2 == 0:
            a = a+ int(s[i+1])
        
    a = int(a/ (len(s)/2))

    for i in range(1,len(s),2):
        if a < s[i]:
            l.append(s[i-1])

    return l       
        

    




"""
Function name: messageEncoder()
Parameters: message (string)
Returns: encodedMessage (string)
"""




            



def messageEncoder(s):
    if s == '':
        return None
    
    i = 0
    a = s.split(' ')
    l = []
    for w in a:
        if i:
            l.append(w.lower())
        else:
            l.append(w.upper())
        i = int(not i)
    return " ".join(l)
    i = 0


             


"""
Function name: courseCreator()
Parameters: courseList (list)
Returns: newCourse (str)
"""

def courseCreator(s):
    import re
    final = 0
    ans =""
    k =[]
    l =[]
    
    if len(s) == 0:
        return None
    for x in s:
        l.append(re.split(r'(^[^\d]+)', x)[1:])
        
    k.append(l[0][0])
    for i in range(0,len(s)):
        final = int(l[i][1])+ final

    final = int(final / len(s))
   
    final =  str(final)    
    k.append(final)

    ans = ans.join(k)
   
    return ans


   
    



"""
Function name: compoundWords()
Parameters: wordsList (list), num (int)
Returns: matchedWords (list)
"""

def compoundWords(a,b):
    if len(a) == 0:
        return None
    k = []
    m = len(a)
    for i in range(0, m):
        for j in range (0, m):
            if i < j and len(a[i])+len(a[j]) == b:
                  k.append(a[i]+a[j])

    return k
    
    


            
            
