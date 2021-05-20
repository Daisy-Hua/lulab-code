import sys


input = sys.argv[1]
output = sys.argv[2]

f1 = open(input, 'r')
lines = f1.readlines()
#第一行lines（0）是标签
temp = []
for idx, line in enumerate(lines[1:]):
    line = line.strip().split('\t')
    bound = len(line)
    temp.append(line)

num = len(lines)-1
print(num)

sum = []
result = []
result.append(lines[0])

for x in range(1, bound):
    initial = 0
    for y in range(0, num):
        initial += int(temp[y][x])
    sum.append(str(initial))


sum = '\t'.join(sum)
result.append(lines[0][0] + '\t' + sum + '\n')
       # sum.append(str(int(temp[0][x])+int(temp[1][x])+int(temp[2][x])+int(temp[3][x])+int(temp[4][x])+int(temp[5][x])))

f2 = open(output, 'w')
f2.writelines(result)
f2.close()

