check = 0
for i in range(16):
    line = [int(x) for x in input().split()]
    for j in range(len(line)):
        for k in range(j + 1, len(line)):
            if line[j] % line[k] == 0 or line[k] % line[j] == 0:
                print(j, k)
                check += max(line[j], line[k]) // min(line[j], line[k])
print(check)

