import sys

input1 = sys.argv[1]
bin_length = int(sys.argv[2])
output = sys.argv[3]

f1 = open(input1, 'r')
lines = f1.readlines()
d = {}
file = []

for idx, line in enumerate(lines):
    line = line.strip().split('\t')
    d[line[3] + str(idx + 1)] = line
    file.append('\t'.join(line).replace('exon', 'exon' + str(idx + 1)) + '\n')

for exon in d.keys():
    if int(d[exon][2]) - int(d[exon][1]) <= bin_length:
        bin_length = int(d[exon][2]) - int(d[exon][1])

test_num = 1
for exon in d.keys():
    for i in range(int((int(d[exon][2]) - int(d[exon][1])) / bin_length)):
        if i != int((int(d[exon][2]) - int(d[exon][1])) / bin_length) - 1:
            file.append(d[exon][0] + '\t' + str(int(d[exon][1]) + i * bin_length + i) + '\t' + str(int(d[exon][1]) + (i + 1) * bin_length + i) + '\t' + 'test' + str(test_num) + '\t0\t' + d[exon][5] + '\n')
        else:
            file.append(d[exon][0] + '\t' + str(int(d[exon][1]) + i * bin_length + i) + '\t' + str(int(d[exon][2])) + '\t' + 'test' + str(test_num) + '\t0\t' + d[exon][5] + '\n')
        test_num += 1

f2 = open(output, 'w')
f2.writelines(file)
f2.close()
