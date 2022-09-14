def binarySearch(array, elementToSearch):
    
    array.sort()
    
    begin = 0
    end = len(array) - 1
    
    while (begin <= end):
        mid = (begin + end)//2
        
        if (elementToSearch < mid):
            end = mid
        elif (elementToSearch > mid):
            begin = mid
        else:
            return True
    
    return False

if __name__ == "__main__":
    array = input("Enter list of array elements: ")
    array = array.split()
    array = [ int(i) for i in array ]
    
    searchelement = input("Enter element to be searched in array: ")
    searchelement = int(searchelement)
    
   if binarySearch(array, searchelement):
        print("binarySearch : Element is present in array\n")
    else:
        print("binarySearch : Element is not present in array\n")
