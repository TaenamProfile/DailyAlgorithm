from collections import Counter

arr = []
for _ in range(10):
    arr.append(int(input())%42)
#print(Counter(arr))
print(len(Counter(arr)))
