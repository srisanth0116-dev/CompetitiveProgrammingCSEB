n = int(input())
arr = list(map(int, input().split()))

count = [0] * 100

for num in arr:
    count[num] += 1

print(*count)

