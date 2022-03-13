# Display Fibonacci series up to 10 terms

f = 0
s = 1
t = 1
for i in range(2,12):
    print(f, end=' ') #try manipulating with this line of code, move it up or down, or change the printed variable to f, s, or t
    t = f + s
    f = s
    s = t
