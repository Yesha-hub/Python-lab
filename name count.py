f=open("Assignment.txt","r")
data=str(f.readlines())
print(data)
y=data.split()
print(y)
print(y.count("yesha"))


output
['study yesha in pdeu \n', 'i am yesha gor\n', 'i yesha like dancing\n']
["['study", 'yesha', 'in', 'pdeu', "\\n',", "'i", 'am', 'yesha', "gor\\n',", "'i", 'yesha', 'like', "dancing\\n']"]
3
