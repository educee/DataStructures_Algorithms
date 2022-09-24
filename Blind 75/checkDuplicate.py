#Given Array of Integers, check if it contains duplicates (leetcode 217)

#Brute force approach Time : O(n2) and Space : O(1)
#For each element in array check all other elements for duplicate everytome

def checkDuplicate(arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
            
    return False

#Next better aproach is to sort array which takes nlogn time and in sorted array duplicate elements are 
#present adjecent to other 

def checkDuplicate_sort(arr):
    arr = sort(arr)
    
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return True
        
    return False

#Another aproach is with time complexity of O(n) with O(n) space

def checkDuplicate_hashset(arr):
    hashset = {}
    for element in arr:
        if element in hashset.keys():
            return True
        else:
            hashset[element] = True
            
    return False

#Using set data strucuture, as set data structure contains NO duplicats -- if array contains duplicate, 
# set stores only one element , therefore array length changes,  compare len of arr and set to verify

def checkDuplicate_usingSet(arr):
    return len(arr) != len(set(arr))
        

if __name__ == '__main__':
    arr = input("Enter Array Elements : ")
    arr = arr.split()
    arr = [int(i) for i in arr]
    
    print("Brute Force Approach:")
    print("=====================")
    if checkDuplicate(arr):
        print("Array Contains Duplicates")
    else:
        print("Array Does Not Contains Duplicates")
        
    print("Sorting Array Approach:")
    print("=====================")
    if checkDuplicate(arr):
        print("Array Contains Duplicates")
    else:
        print("Array Does Not Contains Duplicates")
        
    print("hashmap Approach:")
    print("=====================")
    if checkDuplicate(arr):
        print("Array Contains Duplicates")
    else:
        print("Array Does Not Contains Duplicates")
        
    print(checkDuplicate_usingSet(arr))
        
