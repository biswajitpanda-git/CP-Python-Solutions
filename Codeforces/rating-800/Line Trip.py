import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index]) # number of test cases
index += 1

results = []
for _ in range(t):
    n = int(data[index]) # number of gas stations
    x = int(data[index + 1]) # destination point
    index += 2

    # list to store point including start, gas stations, and destination
    points_list = [0]

    # loop through each gas station
    for _ in range(n):
        point = int(data[index])
        points_list.append(point)
        index += 1
    
    points_list.append(x) # append destination to points
    n = len(points_list)
    max_distance_between_stations = -float('infinity')

    # loop through each point
    for i in range(1, n):
        if i == n-1:
            max_distance_between_stations = max(max_distance_between_stations, 2*(points_list[i] - points_list[i - 1]))
        else:
            max_distance_between_stations = max(max_distance_between_stations, (points_list[i] - points_list[i - 1]))

    results.append(max_distance_between_stations)
for result in results:
	print(result)
    