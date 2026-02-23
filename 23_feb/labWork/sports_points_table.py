points = list(map(int, input("Enter team points: ").split()))

for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

points.sort(reverse=True)

print("Winner Points:", points[0])
print("Runner-up Points:", points[1])
print("Leaderboard:", points)