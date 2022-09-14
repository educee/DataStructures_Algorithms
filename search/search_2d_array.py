def search_2d_array(array, elementToSearch):
    
    for row in range(len(array)):
        for col in range(len(array[row])):
            if elementToSearch == array[row][col]:
                return True
            
    return False
if __name__ == "__main__":
    print("Enter list of Arrays \(2D array\)\n")
    print("Enter size of array\n")
    array_size = int(input())
    array = []
    for i in range(array_size):
        row = input("Enter row : ")
        row = row.split()
        row = [ int(i) for i in row]
        array.append(row)

    searchelement = input("Enter element to be searched in array: ")
    searchelement = int(searchelement)

    #print(array)
    if search_2d_array(array, searchelement):
        print("Element is present in array\n")
    else:
        print("Element is not present in array\n")
