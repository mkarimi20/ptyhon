# Find the maximum of the list of given number

def max_finder2(a,b):
    if  a > b:
        return a
    return b
    
def max_finder3(a,b,c):
    return max_finder2(a, max_finder2(b,c))
print(max_finder3(3,7,-7))