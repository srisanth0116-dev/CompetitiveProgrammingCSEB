n = int(input())
arr = list(map(float, input().split()))

mn = min(arr)
mx = max(arr)

if mn == mx:
    print(*arr)
else:
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int((num - mn) * (n - 1) / (mx - mn))
        buckets[index].append(num)

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    if all(x.is_integer() for x in result):
        print(*map(lambda x: int(x), result))
    else:
        print(*["{:.2f}".format(x) for x in result])

