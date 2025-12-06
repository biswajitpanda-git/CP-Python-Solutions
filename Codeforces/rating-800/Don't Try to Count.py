import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):

    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    
  
    x = data[index]
    index += 1
    s = data[index]
    index += 1
    
    found = False
    
    # Try up to 6 operations. 
    
    # Why 6? Because n*m <= 25. 2^5 = 32, which covers the length requirement.
    # We add 1 extra op to cover cases where 's' is split across the seam.
    for op in range(6):
        
        if s in x:
            print(op)
            found = True
            break
        
        # if not found, append x to itself for the next check
        x += x
    
    # if we finished the loop and never found it
    if not found:
        print("-1")