x = [1,2,3,4,5]
y = []
w = [ i for i in x if i%2==1]
for i in x:
    y.append(i**2)

z = [i**2 for i in y]

print (x)
print (y)
print (z)
print (w)