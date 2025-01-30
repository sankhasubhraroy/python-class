# Break
# The break statement is used to exit or "brake" out of a loop
# When the break statement is executed, the program immediately exits the loop, and the control moves to the next line of code
for i in range(5):
    if i == 2:
        break
    print(i)

print()
# Continue
# the Continue statement is used to skip the current iteration of the loop
# while skipping the rest of the code inside the loop, and the next iteration of the loop begins
for i in range(10):
    if i == 4:
        continue
    elif i == 8:
        break
    print(i)

print()
# Pass
# The pass statement is a null operation or a placeholder
# it is used when a statement is syntactically required, but we don't want to execute any code
for i in range(8):
    if i == 3:
        pass
    print(i)
