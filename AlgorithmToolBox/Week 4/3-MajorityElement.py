def majority_element_naive(elements):
    elements_Sort=sorted(elements)
    if len(elements_Sort) ==1:
        return 1
    if len(elements_Sort) == 2:
        if elements_Sort[0]==elements_Sort[1]:
            return 1
        else:
            return 0
    if len(elements_Sort)%2==0:
        last_index = len(elements_Sort)//2+1
    else:
        last_index = len(elements_Sort)//2
    for index, e in enumerate(elements_Sort[:last_index+1]):
        if index+len(elements_Sort)//2 <= len(elements_Sort)-1:
            if elements_Sort[index] == elements_Sort[index+ len(elements_Sort)//2]:
                return 1

    return 0
        # count = 1
        # if element_Sort[index+count] == e:
        #     count +=1
        #     while element_Sort[index+count] ==e and index+count<len(elements)-1:
        #         count+=1
        #     if count > len(elements)/2:
        #         return 1




if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
