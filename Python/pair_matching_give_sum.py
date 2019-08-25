"""
How do you find all pairs of an integer array whose sum is equal to a given number
"""

def printpairs(arr,arr_size,sum):
    s = set()
    for i in range(0,arr_size):
        temp = sum -arr[i]
        if (temp in s):
            print('Pair with given sum '+str(sum)+" is : ("+str(arr[i])+','+str(temp)+")")
            #print("Pair with given sum " + str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])




#run with test
a = [1, 4, 45, 6, 10, 8]
n = 16
print(printpairs(a,len(a),n))