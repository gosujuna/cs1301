'''
CSC104 Assignment 4
Where's Weldo?
'''

# ------------- provided functions
def flatten_list(l):
    '''
    Returns a list of values, where each element in the returned list is
    a non-list.

    The returned list is a flattened version of l, i.e. removing any
    level of nesting and storing the elements in the order which they appear.

    For example:

    >>> l = [[["wow"], \
        [1, "hello", [1, 2, 100, 999, "weldo"]], \
         1, \
         2]]
    >>> flatten_list(l) == ["wow", 1, "hello", 1, 2, 100, 999, "weldo", 1, 2]
    True

    >>> l = ["llama", [1, 2, 999, [55, 5]]]
    >>> flatten_list(l) == ["llama", 1, 2, 999, 55, 5]
    True
    
    '''
    is_flat = True
    for i in range(len(l)):
        if type(l[i]) == list:
            is_flat = False
            return l[0:i] + flatten_list(l[i]) + flatten_list(l[i+1:len(l)])
            
    if is_flat:
        return l[:]
# ---------- end provided functions



def search(list):
    for i in range(len(list)):  #this search function runs through a loop and returns the index of whatever was given as a parameter. returns -1 if its not found
        if list[i] == "weldo":
            return i
    return -1

def wheres_weldo(world):
    blank = [] #make blank answer
    flat = flatten_list(world) #uses flatten function that was given
    ans = search(flat) #Now list is flattended, we use the search function and get the index of it.
    
    if ans == -1 : #if the search function returns -1, the answer was not found so we return the blank list.
        return blank
    else: 
        j = (len(flat)**(1/2)) # length of square list 
        k = int(ans / j)  # uses divide to find how many is in first index
        l = int(ans %  j)  # uses mod to find how many is in second index
        blank.append(k)  
        blank.append(l)  #adds the found index to the blank list.
        return blank

# --------- end your functions here

if __name__ == "__main__":
    import doctest

    # uncomment the line below to run your doctests
    #doctest.testmod()
