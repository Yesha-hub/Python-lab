def isInside(x, y, rad, a, b):
    if ((a - x) * (a- x) +
        (b- y) * (b - y) <= rad * rad):
        print(" True")
    else:
        print(" false")
a = 1; 
b = 5;
x = 0; 
y = 1; 
rad = 2;
if(isInside(x, y, rad, a, b)):
    print(" it is inside Inside");
else:
    print(" it is outside Outside");


output
false
 it is outside Outside
