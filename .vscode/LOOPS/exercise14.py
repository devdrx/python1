# Reverse a given integer number
num = int(input("Enter a number: "))
dup_num = num
d = 0
rev_num = 0
hold_num = 0
while (num > 1):
    num = num/10
    d += 1
print (d)
for i in range (1,d+1):
    hold_num = dup_num%10
    dup_num = int(dup_num/10)
    rev_num += hold_num*(10**(d-i))
    
print("The reversed number is: " , rev_num)    
