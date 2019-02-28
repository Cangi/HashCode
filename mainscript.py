# f = open('data.txt')
# arr = f.read().split()
# n= arr[0]
# print(n)
# f.close()
dic = {}
with open('data.txt','r') as f:
    for line in f:
        real_line = line.split()
        if len(real_line) == 1:
            continue
        t = real_line[0]
        count = real_line[1]
        for i in range(int(count)):
            dic[real_line[2 + i]].append({i, t})
            print(dic[t])
