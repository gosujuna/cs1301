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

world = [["wow"],  [1,"hello", [ 1,2,100,999,"weldo"]], 1, 2, "hi","apple", " banana", "capybara", " anemone", "fish"]

def search(list):
    for i in range(len(list)):
        if list[i] == "weldo":
            return i
    return -1

def wheres_weldo(world):
    blank = []
    flat = flatten_list(world)
    ans = search(flat) 
    print(ans)
    if ans == -1 :
        return blank
    else: 
        j = (len(flat)**(1/2)) # length of square list 
        k  = int(ans / j)
        l = int(ans %  j)
        blank.append(k)
        blank.append(l)
        return blank

print(wheres_weldo(world))

# --------- end your functions here

#if __name__ == "__main__":
    #import doctest

    # uncomment the line below to run your doctests
    #doctest.testmod()
