lst=['madam','python','malayalam',12321]
for i in lst:
    if str(i)==str(i)[::-1]:
        print(i)

output
madam
malayalam
1232
