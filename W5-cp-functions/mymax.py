def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y
    
def max_of_three(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z
        
print(max_of_three(1,2,3))

def listMax(lst):
    max_value=lst[0]
    max_idx=0
    idx=1
    for x in lst[1:]:
        if x>max_value:
            max_value=x
            max_idx=idx
        idx+=1
    return(max_value, max_idx)
print(listMax([0,1,3]))