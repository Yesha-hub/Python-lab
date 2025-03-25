def fun():
    print( "function called ")
def disp():
    print("disp called ")
def msg():
    print (" msg called ")
func=[fun,disp,msg]
for f in func:
    f()

output
function called 
disp called 
 msg called 
