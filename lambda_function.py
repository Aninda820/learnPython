def appl(fx, value):
    return 6+fx(value)

double = lambda y: y*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2

print(double(5))
print(cube(3))
print(avg(3,5))
print(appl(cube, 3))