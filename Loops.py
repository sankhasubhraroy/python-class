# For Loop
arr = [12, 67, 45, 7, 3, 75, 33]
for val in arr:
    print(val)

print()
# Range Function
# The range function is used to generate a sequence of numbers
# It takes 1 or 2 or 3 parameters (start,stop, step)
# start - it defines from to start generating the sequence
# stop - it defines where to stop
# step - it defines the increment pattern to generate sequence
for i in range(2, 10, 2):
    print(i)

print()
# While Loop
count = 0
while count < 3:
    count = count + 1
    print("Hello", count)
