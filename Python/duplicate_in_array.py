"""
How do you find the duplicate number on a given integer array?
"""
def find_repeat(x):
    _size =len(x)
    repeated = []
    print(_size)
    for i in range(_size):
        k = i+1
        for j in range(k,_size):
            if (x[i]==x[j] and x[i] not in repeated):
                repeated.append(x[i])

    return repeated

print(find_repeat([10,11,21,33,44,33,44,66,88,99]))
print(find_repeat([12,44,66,88,6,77,33,77,12,88,44]))