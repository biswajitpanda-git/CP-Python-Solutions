import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])  # number of test cases
index += 1

for _ in range(t):
    n = int(data[index])  # number of segments
    index += 1
    s = data[index]  # string representing segments
    index += 1

    continous_three_empty_cells = False
    total_count_of_empty_cells = 0

    for i in range(n):
        if s[i] == '.' and i+1<n and s[i+1] == '.' and i+2<n and s[i+2] == '.':
            continous_three_empty_cells = True
            break
        if s[i] == '.':
            total_count_of_empty_cells += 1
    if continous_three_empty_cells:
        print(2)
    else:
        print(total_count_of_empty_cells)

