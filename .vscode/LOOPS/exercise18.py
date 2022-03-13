row = 5
i = 0
j = 0

for i in range(0,5):
    for j in range(0,i):
        print("*", end = ' ')
    print(" ")
    
for i in range(5,0,-1):
    for j in range(0,i):
        print("*", end = ' ')
    print(" ")

