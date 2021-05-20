import sys

input1 = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]
input4 = sys.argv[4]
input5 = sys.argv[5]
input6 = sys.argv[6]
input7 = sys.argv[7]
input8 = sys.argv[8]
input9 = sys.argv[9]
input10 = sys.argv[10]
'''
input11 = sys.argv[11]
input12 = sys.argv[12]
input13 = sys.argv[13]
input14 = sys.argv[14]
'''
abundance = [0 for _ in range(10)]
for x in range(1, 11):
    f = open(sys.argv[x], 'r')
    lines = f.readlines()
    del lines[0]

    for idx, line in enumerate(lines):
        line = line.strip().split('\t')
        col_num = len(line)
        for i in range(1, col_num):
            abundance[x-1] += int(line[i])

print(abundance)
