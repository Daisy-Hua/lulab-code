import sys

input = sys.argv[1]
output = sys.argv[2]

f1 = open(input, 'r')
lines = f1.readlines()

temp = []
for idx, line in enumerate(lines[1:]):
    line = line.strip().split('\t')
    bound = len(line)
    temp.append(line)


sum = []

for x in range(1, bound):
    sum.append(str(int(temp[0][x])+int(temp[1][x])+int(temp[2][x])+int(temp[3][x])+int(temp[4][x])+int(temp[5][x])))


sum = '\t'.join(sum)

result = []
result.append(lines[0])
result.append('chr10'+'\t'+sum+'\n')

f2 = open(output, 'w')
f2.writelines(result)
f2.close()

