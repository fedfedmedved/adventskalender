#for this puzzle i'm counting the width of the cut-off of the parabola
# (a-x)x
# Here a is time, x is speed, domain is integers 0<=x<=a

# I can start at the center of the parabola, then proceed to step toward 0
# at each step i count the value and compare with target value
# then i multimply by 2, being careful with the top value.

import re
import math

a = 15
print(a % 2)

#read data as dictionary

time = re.findall('\d+' , 'Time:        34     90     89     86')
time = [int(entry) for entry in time]
print(time)

dist = re.findall('\d+' , 'Distance:   204   1713   1210   1780')
dist = [int(entry) for entry in dist]

data = dict(zip(time , dist))

print(data)

count_prod = 1

for a in time:
    x = math.floor(a / 2)
    y = (a-x)*x
    counter = -1 if x == a/2 else 0
    while y > data[a]:
        counter = counter + 2
        x = x - 1
        y = (a - x) * x
    count_prod = count_prod * counter

print(count_prod)

#### Part 2
a = 34908986
record = 204171312101780

x = math.floor(a / 2)
y = (a-x)*x
counter = -1 if x == a/2 else 0
while y > record:
    counter = counter + 2
    x = x - 1
    y = (a - x) * x
print(counter)