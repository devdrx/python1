# Create a recursive function
# num = 10
# sum = 0
# for i in range(0,num):
#     i = i + 1
#     sum += i
# print(sum)

def addition(num):
    if num:
        return num + addition(num-1)
    else:
        return 0

res = addition(10)
print(res)