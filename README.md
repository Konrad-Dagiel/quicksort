# Python Quicksort implementation

## Basic idea behind quick sort:
while searches not crossed
    search to right from pivot for a bigger item     
    search to left from end for a smaller item
    if searches not crossed
        swap items
swap pivot with most recently found small item
sort(list, small, pivot)
sort(list, pivot+1, end)
