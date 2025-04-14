"""
    CHAPTER 5
    TEST FOUR
        - Filter Odd Even

        * define a function which will take a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        * you have to filter odd even number and 
        * return list in this format: [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
"""
# [1,2,3,4,5,6,5,7,8,9,10]

def filter_numbers(l):
    odd = []
    even = []
    filtered_elements = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even.append(l[i])
            # filtered_elements.append(even)
        else:
            odd.append(l[i])
            # filtered_elements.append(odd)
    filtered_elements.append(odd)
    filtered_elements.append(even)
    return filtered_elements

print(filter_numbers(list(range(1, 11))))
