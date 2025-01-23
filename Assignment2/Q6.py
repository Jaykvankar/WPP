points = []
for i in range(10):
    x, y, z = map(float, input(f"Enter coordinates for point {i + 1} (x y z): ").split())
    points.append((x, y, z))

nearest_neighbors = []
for i in range(len(points)):
    current_point = points[i]
    nearest_point = None
    min_distance = float('inf')
    for j in range(len(points)):
        if i != j:
            dist = ((current_point[0] - points[j][0]) ** 2 + 
                    (current_point[1] - points[j][1]) ** 2 + 
                    (current_point[2] - points[j][2]) ** 2) ** 0.5
            if dist < min_distance:
                min_distance = dist
                nearest_point = points[j]
    nearest_neighbors.append((current_point, nearest_point))

print(nearest_neighbors)
