# Calculate the sum of all numbers from 1 to a given number
number = int(input(("Enter your number: ")))
i = 1
sum = 0
for i in range(1, number+1, 1):
    sum += i

print("the sum is " + str(sum))
