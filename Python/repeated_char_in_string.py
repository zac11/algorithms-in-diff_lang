check_string = "i am checking this string to see how many times each character appears"
count = {}
for s in check_string:
    if s in count:
        count[s]+=1
    else:
        count[s]=1

for key in count:
    if count[key] > 1:
        print (key, count[key])