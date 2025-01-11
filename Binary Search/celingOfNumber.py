# Given a sorted array and a value x, the ceiling of x is the 
# smallest element in an array greater than or equal to x, 
# and the floor is the greatest element smaller than or equal to x

def floorOfNum(arr, target):
    start = 0
    end = len(arr) - 1 

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1 
            
        elif arr[mid] > target:
            end = mid - 1 

        else:
            return mid 

    return end

def celingOfNumber(arr, target):
    start = 0
    end = len(arr) - 1 

    if target > arr[end]:
        return -1 

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1 
            
        elif arr[mid] > target:
            end = mid - 1 

        else:
            return mid 

    return start


arr = [4,5,6,8,13,15]
result = celingOfNumber(arr, 19)
print(result)
result = floorOfNum(arr, 3)
print(result)

