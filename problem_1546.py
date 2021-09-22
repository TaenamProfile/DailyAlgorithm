examCount = int(input())
a = map(int,input().split())
b = 0

for i in range(examCount):
    int(a[i])
    b += a[i]

M = max(a)
print(b/M * 100/examCount)