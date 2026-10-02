n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

arr = sorted(a + b)

l = len(arr)

if l % 2 != 0:
     M=(arr[l//2])
else:
     M=((arr[l//2 - 1] + arr[l//2]) / 2)
print(f"{M:.1f}")

