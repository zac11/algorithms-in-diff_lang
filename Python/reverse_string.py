def reverseString(s):
    str = ''
    for i in s:
        str =   i+str
    return str


s = "RahulYadav"
print("Original string",end=" ")
print(s)
print('Reversed string is',end=" ")
print(reverseString(s))


"""
Use recursion
"""
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]+s[0])

s = "AnubhaKabalia"
print("Original string",end=" ")
print(s)
print('Reversed string is',end=" ")
print(reverseString(s))


"""
reversed method
"""
def stringrev(s):
    string = "".join(reversed(s))
    return string


s = "ReversePrinting"
print("Original string",end=" ")
print(s)
print('Reversed string is',end=" ")
print(reverseString(s))

