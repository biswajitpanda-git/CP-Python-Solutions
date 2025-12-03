import sys 

input = sys.stdin.read
data = input().split()

index = 0
t=int(data[index])

for i in range(1, t+1):
    n = int(data[i])
    if n%3==0:
        print("Second")
    else:
        print("First")

#TC - O(1)
#SC - O(1)