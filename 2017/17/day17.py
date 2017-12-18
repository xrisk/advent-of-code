skip = int(input())
ls = [0]
list_size = 1
pos = 0

for i in range(1, 2018):
    pos = (pos + skip) % list_size
    ls.insert(pos + 1, i)
    list_size += 1
    pos += 1

print(ls[pos + 1])


