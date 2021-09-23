examCount = int(input())
a = list(map(int, input().split()))
b = 0

for i in range(examCount):
    x = a[i]
    b += x

M = max(a)
print(b/M * 100/examCount)
