A, B = map(int, input().split())

if A == 0:
    print(B)
elif B == 0:
    print(A)
else:
    shift = 0

    while ((A | B) & 1) == 0:
        A >>= 1
        B >>= 1
        shift += 1

    while (A & 1) == 0:
        A >>= 1

    while B != 0:
        while (B & 1) == 0:
            B >>= 1

        if A > B:
            A, B = B, A

        B = B - A

    print(A << shift)

