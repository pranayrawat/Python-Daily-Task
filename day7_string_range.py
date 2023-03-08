def string_range(num):
    l1 = [str(i) for i in range(num)]
    return ".".join(l1)

print(string_range(6))