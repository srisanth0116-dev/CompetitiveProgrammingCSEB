A, B = map(int, input().split())

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


D, x0, y0 = extended_gcd(A, B)


p = B // D
q = A // D

candidates = set()

k1 = -x0 / p
candidates.add(int(k1))
candidates.add(int(k1) + 1)

k2 = y0 / q
candidates.add(int(k2))
candidates.add(int(k2) + 1)

best = None

for k in candidates:
    x = x0 + k * p
    y = y0 - k * q

    current = (abs(x) + abs(y), x > y, x, y)

    if best is None or current < best:
        best = current

x = best[2]
y = best[3]

print(x, y, D)

