
#do not care about the insertion seq
t=[12,44,55,66,77,55,33,44,11,23,11,88]
from collections import OrderedDict
print(list(OrderedDict.fromkeys(t)))

