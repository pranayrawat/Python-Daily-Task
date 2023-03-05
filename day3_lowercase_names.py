names = ['carol','adam','Rose','Mary','John','dickson','kerry']
ans = []

for i in names:
    if i.islower():
        ans.append(i)

ans.sort(reverse=True)
ans = tuple(ans)

print(ans)

