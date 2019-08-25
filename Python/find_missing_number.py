"""

You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list.
 Write an efficient code to find the missing integer.
"""

def missing_number(num_list):
    orig_list = [x for x in range(num_list[0],num_list[-1]+1)]
    num_list = set(num_list)
    return (list(num_list ^ set(orig_list)))

print(missing_number([1,2,3,4,6,7,8,9]))
print(missing_number([1,2,4,5,7,8,9]))