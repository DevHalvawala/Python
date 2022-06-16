from itertools import combinations


# Get a list of numbers from input
numbers = [int(n) for n in input().split()]
# Get K value from input
k = int(input())
# Count combinations that sum to K
count = 0
# Try combinations of all possible sizes
for i in range(1, len(numbers)+1):
    # Try all combinations of size i
    for c in combinations(numbers, i):
        # If this combination sums to K, then increase the count
        if sum(c) == k:
            count += 1
# Output the count
print(count)