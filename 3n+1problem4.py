i, j = map(int, input().split())

oi, oj = i, j  
if i > j:
    i, j = j, i

max_cycle = 0

for n in range(i, j + 1):
    num = n
    cycle = 1

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        cycle += 1

    if cycle > max_cycle:
        max_cycle = cycle

print(oi, oj, max_cycle)
    
    
 

