#In this case, filter returns the elements for which the function returns 'true'
#The filter resembles a for loop but it is a builtin function and faster.
numbers = range(-100, 100)
negatives = list(filter(lambda x: x>0, numbers))
print(negatives)