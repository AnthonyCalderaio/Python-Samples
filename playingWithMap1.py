/////////////////////////////////////

def addition(n):
    return n*2
    
numbers = (2,3,67,32)
results = map(addition, numbers)
print(list(results))

/////////////////////////////////////

def addition(x, y, z):
    return x*y*z
    
numbers1 = [2,3,67,32]
numbers2 = [1,2,3,4]
numbers3 = [1,2,3,4]
results = map(addition , numbers1, numbers2, numbers3)
print(list(results))

//////////////////////////////////////