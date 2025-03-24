x=int(input(" enter marks of physics "))
y=int(input(" enter marks of chemistry "))
z=int(input(" enter marks of maths "))
sum=x+y+z
print(" the total is ",sum)
avg=sum/3
print(" the average is ",avg)
if sum>80 & sum<100:
    print(" O grade ")
elif sum>70 & sum<90:
    print(" A+ grade ")
elif sum>60 & sum<69:
    print(" A grade ")
elif sum>55 & sum<59:
    print(" B+ grade ")
elif sum>50 & sum<54:
    print(" B grade ")
elif sum>45 & sum<49:
    print(" C grade ")
elif sum>40 & sum<44:
    print(" P grade ")
elif sum>0 & sum<39:
    print(" F grade ")


output
enter marks of physics 87
 enter marks of chemistry 88
 enter marks of maths 89
 the total is  264
 the average is  88.0
 O grade 
