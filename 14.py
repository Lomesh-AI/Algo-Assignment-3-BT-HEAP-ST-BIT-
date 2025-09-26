import heapq
n = int(input())                  # Reading input from STDIN
arr = list(map(int, input().split()))

min_heap = []
mul = 1

for i in range(n):
    heapq.heappush(min_heap, arr[i])
    mul *= arr[i]

    if len(min_heap) < 3:
        print(-1)

    elif len(min_heap) > 3:
        mul //= heapq.heappop(min_heap)
        print(mul)
    else:
        print(mul)        