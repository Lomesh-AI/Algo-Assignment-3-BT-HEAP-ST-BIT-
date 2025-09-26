import heapq
_, vacant = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

# print(rows, vacant, arr)

max_heap = []
for i in arr:
    heapq.heappush(max_heap, -i)

cost = 0
while vacant:
    curr = -heapq.heappop(max_heap)
    cost += curr
    # print(cost)
    if curr > 1:
        heapq.heappush(max_heap, -(curr - 1))
    vacant -= 1
print(cost)   
