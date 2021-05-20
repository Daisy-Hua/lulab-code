import sys
import numpy as np


input = sys.argv[1]
total_reads = sys.argv[2]
total_label = sys.argv[3]
output = sys.argv[4]


temp = []
#peak split & length calculation
f1 = open(input, 'r')
lines = f1.readlines()
label = lines[0].strip().split('\t')
label = label[1:]
for x in label:
    x = x.strip('_')
    temp.append(x)

#totalreads split
tr = []
f3 = open(total_reads, 'r')
lines2 = f3.readlines()
for y, read in enumerate(lines2):
    read = read.strip().split('\t')
    tr = np.array(read[1:], dtype=float)


#label split
f4 = open(total_label, 'r')
lines3 = f4.readlines()
match = lines3[0].strip().split('\t')
match = match[1:]

def FPKM(lines, x):
    line_temp = lines[x].strip().split('\t')
    lengthinfo = line_temp[0].strip().split('|')
    length = int(lengthinfo[2])-int(lengthinfo[1])
    line_replace = np.array(line_temp[1:], dtype=float)

    temp2 = []
    for idx, x in enumerate(line_replace):
        for idx2, y in enumerate(match):
            if temp[idx] == y:
                if tr[idx2] != 0:
                    x = x * 10**6 * 10**3 / (tr[idx2] * 2 * length)
                    temp2.append(x)
                else:
                    x = 0.0
                    temp2.append(x)

    temp3 = []
    for x in temp2:
        temp3.append(str(x))

    out = []
    out.append(line_temp[0] + '\t' + '\t'.join(temp3).replace('nan', '0.0') + '\n')
    return(out)

out = []
out.append(lines[0])
for chr, region in enumerate(lines[1:]):
    out.append(''.join(FPKM(lines, chr+1)))


f2 = open(output, 'w')

f2.writelines(out)

f2.close()











