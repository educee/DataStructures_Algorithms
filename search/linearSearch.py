def linearSearch(array, elementToSearch):

    for item in array:
        if item == elementToSearch:
            return True

    return False
if __name__ == "__main__":
    array = input("Enter list of array elements: ")
    array = array.split()
    array = [ int(i) for i in array ]
    
    searchelement = input("Enter element to be searched in array: ")
    searchelement = int(searchelement)
    
    if linearSearch(array, searchelement):
        print("LinearSearch : Element is present in array\n")
    else:
        print("LinearSearch : Element is not present in array\n")
