"""
How to find largest and smallest number from integer array - Java Solution

"""
lst = []
num = int(input('How many numbers :'))
for n in range(num):
    numb = int(input('Enter the number : '))
    lst.append(numb)

print('Max is ',max(lst))
print('Min is ',min(lst))