ratings = list(map(int, input("Enter ratings (1-5): ").split()))

valid = []
for r in ratings:
    if 1 <= r <= 5:
        valid.append(r)

if len(valid) == 0:
    print("No valid ratings.")
else:
    print("Average Rating:", sum(valid)/len(valid))
    print("5 Star Ratings:", valid.count(5))
    valid.sort()
    print("Sorted Ratings:", valid)