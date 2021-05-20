import sys

input = sys.argv[1]
r = int(sys.argv[2])#r stands for combination number the user wants
output = sys.argv[3]

origin = open(input, 'r')
lines = origin.readlines()

result = []
result.append(lines[0])
lines = lines[1:]
# n stands for total peak in the origin file
n = len(lines)

def sumup(lines):
    temp = []
    length_sum = 0
    for idx, line in enumerate(lines[0:]):
        line = line.strip().split('\t')
        print(line[0])
        length = []
        length = line[0].strip().split('|')
        length_sum += int(length[2])-int(length[1])
        bound = len(line)
        temp.append(line)
    print(length_sum)
    num = len(lines)

    sum = []
    result = []

    for x in range(1, bound):
        initial = 0
        for y in range(0, num):
            initial += int(temp[y][x])
        sum.append(str(initial))

    sum = '\t'.join(sum)
    result.append(lines[0][0:4] + '|' + '0' + '|' + str(length_sum) + '\t' + sum + '\n')
    return result

if r==5:
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1, n):
                    for m in range(l+1,n):
                        print(i + 1, j + 1, k + 1, l + 1, m + 1)
                        select = []
                        select.append(lines[i])
                        select.append(lines[j])
                        select.append(lines[k])
                        select.append(lines[l])
                        select.append(lines[m])
                        result.append(''.join(sumup(select)))
    select = []

if r==4:
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1, n):
                    print(i + 1, j + 1, k + 1, l + 1)
                    select = []
                    select.append(lines[i])
                    select.append(lines[j])
                    select.append(lines[k])
                    select.append(lines[l])
                    result.append(''.join(sumup(select)))
    select = []


if r==3:
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                print(i+1,j+1,k+1)
                select = []
                select.append(lines[i])
                select.append(lines[j])
                select.append(lines[k])
                result.append(''.join(sumup(select)))

if r==2:
    for i in range(0, n):
        for j in range(i + 1, n):
            print(i + 1, j + 1)
            select = []
            select.append(lines[i])
            select.append(lines[j])
            result.append(''.join(sumup(select)))


result = ''.join(result)

f2 = open(output, 'w')
f2.writelines(result)
f2.close()