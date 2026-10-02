a=int(input(""))
arr1=list(map(int,input().split()))
b=int(input(""))
arr2=list(map(int,input().split()))
merge=arr1+arr2
merge.sort()
print(*merge, sep=" ")

