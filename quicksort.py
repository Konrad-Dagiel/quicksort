"""
Author: Konrad Dagiel
"""

#initialize test list with duplicates
l=[41,37,35,62,29,39,54,27,60,25,40,56,51,48,43,51,51,43]

def quicksort(l):
    """
    runs first iteration, uses first number in list as pivot
    in place algorithm, done with sublists

    l: (list) input list

    return sorted list
    """
    start=0
    end=len(l)-1
    ret=_quicksort(l,start,end)
    return ret

def _quicksort(l, start, end):
    """
    helper function

    l: (list) input list full
    start: (int) index of start of sublist to be sorted
    end: (int) index of end of sublist to be sorted
    """
    if start>=end:
        return l
    pivotv=l[start]
    pivoti=start
    p0=start
    p1=end
    while p0<p1:
        while l[p0]<=pivotv and p0<end:
            p0+=1
        while l[p1]>=pivotv and p1>start:
            p1-=1

        if p0<p1:
            l[p0],l[p1]=l[p1],l[p0]
    l[pivoti],l[p1]=l[p1],l[pivoti]
    pivoti=p1
    
    #iterate over the two sublists, one before the pivots final location, and one after
    _quicksort(l,start,pivoti-1)
    _quicksort(l,pivoti+1, end)

    return l
if __name__=="__main__":
    print(quicksort(l))