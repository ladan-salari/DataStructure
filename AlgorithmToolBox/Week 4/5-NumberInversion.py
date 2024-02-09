from itertools import combinations

def mergeSort(a, n):
    temp_a = [0]*n
    return inversions_naive(a, temp_a, 0, n-1)


def inversions_naive(a, temp_a, left, right):
    number_of_inversions = 0
    if left < right:
        mid = (left + right)//2
        number_of_inversions += inversions_naive(a, temp_a, left, mid)
        number_of_inversions += inversions_naive(a, temp_a, mid+1, right)
        number_of_inversions += merge(a, temp_a, left, mid, right)
    return number_of_inversions

def merge(a, temp_a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    numberinversions = 0

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp_a[k] = a[i]
            i += 1
            k += 1
        else:
            temp_a[k] = a[j]
            j += 1
            k += 1
            numberinversions += mid-i+1


    while i <= mid:
        temp_a[k] = a[i]
        i += 1
        k += 1

    while j <= right:
        temp_a[k]=a[j]
        j += 1
        k += 1
    for i in range(left,right+1):
        a[i]=temp_a[i]
    return numberinversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(mergeSort(elements, len(elements)))
