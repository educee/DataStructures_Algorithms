#Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

 

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

#Brute Force Approach
# time O(n2), Space : O(1)

def twoSum_bruteForce(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == target:
                return [i, j]
            
    return -1

#Sort array and use 2 pointed method on array and increase/decrease pointers to match up to sum
# time : O(nlog(n)),  space : O(1)

def twoSum_sort(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while (left < right):
        print(left, right)
        curSum = arr[left] + arr[right]
        
        if curSum < target:
            left += 1
        elif curSum > target:
            right += 1
        else:
            return [left, right]
    return -1
            
def twoSum(arr: list[int], target: int) -> list[int]:
    prevNums = {}
    
    for idx in range(len(arr)):
        required_num = target - arr[idx]
        if required_num in prevNums.keys():
            return [prevNums[required_num], idx]
        else:
            prevNums[arr[idx]] = idx
            
    return -1

if __name__ == '__main__':
    arr = input("Enter Array Elements : ")
    arr = arr.split()
    arr = [ int(i) for i in arr]
    
    target = input("Enter target sum : ")
    target = int(target)
    
    print(twoSum(arr, target))
    print(twoSum_bruteForce(arr, target))
    print(twoSum_sort(arr, target))
