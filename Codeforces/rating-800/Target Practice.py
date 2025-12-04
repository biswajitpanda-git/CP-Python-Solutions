import sys

# 1. Read all input at once
input_data = sys.stdin.read().split()
idx = 0

if input_data:
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        total_score = 0
        
        # We need to process the next 10 strings (rows)
        # We loop through rows 0 to 9
        for r in range(10):
            row_string = input_data[idx]
            idx += 1
            
            # Loop through columns 0 to 9
            for c in range(10):
                if row_string[c] == 'X':
                    # Calculate how deep this X is inside the target
                    # It is determined by the minimum distance to any of the 4 borders
                    distance_to_edge = min(r, 9 - r, c, 9 - c)
                    
                    # Points = distance + 1 (Edge is distance 0, but worth 1 point)
                    points = distance_to_edge + 1
                    
                    total_score += points
                    
        print(total_score)