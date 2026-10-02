def solve(A):
    n = len(A)

    dp = [0] * n

    for i in range(n - 1, -1, -1):
        prev = 0
        dp[i] = 1

        for j in range(i + 1, n):
            temp = dp[j]

            if A[i] == A[j]:
                dp[j] = prev + 2
            else:
                dp[j] = max(dp[j], dp[j - 1])

            prev = temp

    return dp[n - 1]


A = input().strip()
print(solve(A))

