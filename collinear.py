def collinear(a, b, c, d, e, f):
    x = a * (d - f) + c * (f - b) + e * (b - d)
    if (x == 0):
        print "Yes it is collinear"
    else:
        print "No it is not a collinear"
a, b, c, d, e, f = 1, 1, 1, 1, 4, 5
collinear(a, b, c, d, e, f)

output
Yes it is collinear
