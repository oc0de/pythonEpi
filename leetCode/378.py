'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

'''

from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        minHeap = []
        def push(i,j):
            if i < len(matrix) and j < len(matrix[0]):
                heappush(minHeap, (matrix[i][j],i,j))

        push(0,0)
        pairs = []
        while minHeap and len(pairs) < k:
            m, i, j = heappop(minHeap)
            pairs += m,
            push(i,j+1)
            if j == 0:
                push(i+1,j)

        return pairs[-1]