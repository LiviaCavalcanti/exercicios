import math

def calculateDistanceTwoPoints(p1, p2):
    return int(math.sqrt((p2 - p1)**2))


n_cities = int(input())

distances = list(map(int, input().split(" ")))

max_dist = 0
min_dist = 0

for i in range(n_cities):
    if(i == 0):
        min_dist = calculateDistanceTwoPoints(distances[0], distances[1])
        max_dist = calculateDistanceTwoPoints(distances[0], distances[n_cities-1])
    elif(i == (n_cities-1)):
        min_dist = calculateDistanceTwoPoints(distances[i], distances[i-1])
        max_dist = calculateDistanceTwoPoints(distances[i], distances[0])
    
    else:
        right_neib_dist = calculateDistanceTwoPoints(distances[i], distances[i+1])
        left_neib_dist =  calculateDistanceTwoPoints(distances[i], distances[i-1])
        min_dist = min(right_neib_dist, left_neib_dist)

        dist_to_end = calculateDistanceTwoPoints(distances[i], distances[n_cities-1])
        dist_to_begin = calculateDistanceTwoPoints(distances[i], distances[0])
        max_dist = max(dist_to_end, dist_to_begin)

    print(min_dist, max_dist)


