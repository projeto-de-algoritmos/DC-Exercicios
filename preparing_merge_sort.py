n = int(input())
ans = []
line = input().split()
for num in line:
    a = int(num)
    l, r = 0, len(ans)
    while l != r:
        mid = (l + r) // 2
        if ans[mid][-1] < a:
            r = mid
        else:
            l = mid + 1
    if l == len(ans):
        ans.append([a])
    else:
        ans[l].append(a)

for i in ans:
    for j in i:
        print(j, end=' ')
    print()
