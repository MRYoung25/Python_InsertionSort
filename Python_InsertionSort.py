data = [1, 3, 4, 6, 8, 7, 2, 5, 10, 11, 9, 13, 12]
def InsertionSort(L):
    length = len(L)
    if length == 0 or length == 1:
        return L
    
    for i in range(len(L)-1, 0 , -1):
        current = i
        j = i - 1
        for j in range(j, 0, -1):
            if L[j] > L[current]:
                (L[current],L[j]) = (L[j], L[current])
    return L
pass

print InsertionSort(data)
