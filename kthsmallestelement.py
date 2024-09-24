"""

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

"""

def kthSmallest(matrix, k):
    n = len(matrix)
    print(n, '----------------------n------------------')
    
    # Binary search on the value range
    left, right = matrix[0][0], matrix[n - 1][n - 1]
    
    def count_less_equal(x):
        # This function counts the number of elements less than or equal to x
        count, row, col = 0, n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= x:
                count += (row + 1)  # All elements in this row from 0 to row are <= x
                col += 1
            else:
                row -= 1
                
        return count
    
    while left < right:
        mid = (left + right) // 2
        print(mid, '------------------------------mid------------------------')
        if count_less_equal(mid) < k:
            left = mid + 1
            print(left, '-------------------left-----------------')
        else:
            right = mid
            print(right, '---------------------right----------------')
    print(left, '------------------------------left-------------------------------')
    return left


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

kthSmallest(matrix, k)







