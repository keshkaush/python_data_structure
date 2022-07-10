# heap sort in mainly used  for priority Queues. In python they are created using heapq libary that give you access
# to some inbuilt methods of heapq class like, heapify, heappush, heapreplace, heappop.

import heapq;

if __name__ == "__main__":
    heap = [5, 6, 8, 1, 9, 7, 2]
    heapq.heapify(heap)

    heapq.heappush(heap, 0)

    print(heap)

    print(heapq.heappop(heap))

    print(heap)

    heapq.heapreplace(heap, 3)

    print(heapq.heappushpop(heap, 1))

    print(heap)

    