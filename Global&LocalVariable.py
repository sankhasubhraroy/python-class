def f():
    # local variable (Only accessible inside the scope)
    l = "Local"
    print(l + " " + g)


# Global variable (Accessible from anywhere)
g = "Global"

f()
print(g)
