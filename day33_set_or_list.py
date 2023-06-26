from datetime import datetime
import time
 
look = int(input("look for: "))
t1 = time.time()

for i in set(range(10000000)):
    if i == look:
        t2 = time.time()
        break
    t2 = time.time()
# time.sleep(3)

print(f"t1: {t1}")
print(f"t2: {t2}")

t1_ts = datetime.fromtimestamp(t1)
t2_ts = datetime.fromtimestamp(t2)

delta = t2_ts - t1_ts
print(f"Time taken in set: {delta.total_seconds()}")

#################################

t3 = time.time()
for i in list(range(10000000)):
    if i == look:
        t4 = time.time()
        break
    t4 = time.time()
# time.sleep(3)

print(f"t3: {t3}")
print(f"t4: {t4}")

t3_ts = datetime.fromtimestamp(t3)
t4_ts = datetime.fromtimestamp(t4)

delta2 = t4_ts - t3_ts
print(f"Time taken in list: {delta2.total_seconds()}")

if delta > delta2:
    print("List is faster, so I would choose list")
else:
    print("Set is faster, so I would choose set")