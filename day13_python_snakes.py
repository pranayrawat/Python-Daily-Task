def python_snakes(n):
    for i in range(1,n):
        print(" "*(n-i),end="")
        for j in range(i):
            print("* ",end="")     
        print()
    return ""
print(python_snakes(7))