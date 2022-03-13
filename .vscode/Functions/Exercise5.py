# Create an inner function to calculate the addition in the following way
def outer(a, b):
    def inner(a, b):
        return(a+b)
    sum = inner(a,b)
    return (sum+5)

print(outer(5,10))