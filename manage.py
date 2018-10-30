results = ""
for x in range(2000, 3200):
    if x % 7 == 0:
        y = x / 5.0
        if y % 5 != 0:
            results = results + str(x) + ","

print(results)

results = ""
for x in range(2000, 3200):
    if x % 7 == 0 and y % 5 != 0:
            results = results + str(x) + ","

print(results)

nums = [i for i in range(2000, 3200) if (i % 7) == 0 and (i % 5) != 0]