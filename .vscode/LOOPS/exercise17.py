# Find the sum of the series upto n terms
n = 5
start = 2
sum = 0
for i in range(0,n):
    print(start, end = '+')
    sum += start
    start = start*10 + 2
print(" ")
print("the sum of the above series is: " , sum)