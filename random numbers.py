import random
lst=[random.randint(-15,15) for i in range(11)]
x=map(lambda a: a**2,lst)
print(list(x))


output
[1, 16, 81, 169, 0, 81, 121, 169, 49, 4, 4]
