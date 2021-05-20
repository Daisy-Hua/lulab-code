import sys
import re

input = sys.argv[1]
output = sys.argv[2]

f1 = open(input, 'r')
lines = f1.readlines()
sep = []
for line in lines:
    line = line.strip().split('\t')
    sep.append(line)

lines = list(zip(*sep))


file = []
file.append(lines[0])

for line in lines:
    if re.match('HCC.*', line[0]) != None:
        file.append(line)
    if re.match('NC.*', line[0]) != None:
        file.append(line)

file = list(zip(*file))

out = []

for x in file:
    out.append(x[0] + '\t' + '\t'.join(x[1:]) + '\n')

f2 = open(output, 'w')
f2.writelines(out)
f2.close()

