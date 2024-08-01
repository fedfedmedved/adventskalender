import re
import numpy as np

data = open('day5.txt').read().split('\n\n') #split file at empty lines
data = [item.splitlines() for item in data]

#i'd probably like to define a set of functions that preform all the appropriate conversions for me.
# time to revise

#seed-to-soil map:
# 1  |->  1
# 49 |-> 49
# 98 |-> 50
# 99 |-> 51
# 50 |-> 52
# 97 |-> 99
# for x in seed [1;49] y=x (Id); [50; 97] map is x+2; for x in [98; 99] y=x-48
# would like to have a test for the map to be properly defined - how? they did it in assignments in coursera - it was very nice

#need to split data into maps. using regex? using split?

#data[3] = [int(number) for number in data[3].split(' ')]
#data[4] = [int(number) for number in data[4].split(' ')]

#data[3] = range(data[3][1], data[3][1] + data[3][2]), data[3][0] - data[3][1]

#want to do this for every line after the work 'map' until the next map

data[0] = [range( int(seeds), int(seeds)+int(ranges) ) for seeds, ranges in re.findall('(?P<seeds>\d+)(?:\ )(?P<ranges>\d+)', data[0][0])]
print(data[0])

j=1
while j!=len(data):
    i=1
    while i!=len(data[j]):
        line = data[j][i]
        line = [int(number) for number in line.split(' ')]
        line = range(line[1], line[1] + line[2]), line[0] - line[1]
        data[j][i] = line
        i = i+1
    j = j+1

#data[0] = [int(seeds) for seeds in re.findall('\d+', data[0][0])] #seeds pt1


print(data)

x = data[0] #take seed ranges as function input
for map in data[1:]:
    y=[]
    print(map[0])
    #y = x
    #pass in ranges that were outputs from previous maps
    #alternatively, take all ranges (not a set, repeated elements are allowed) and one input range
    # sort points lowest to highest, keeping track of start and end. now, look left of input.start. is it a start?
    for input in x:
        for interval, offset in map[1:]:
            if input.start in interval:
                output = range(input.start + offset, min(interval.stop, input.stop) + offset)
                y.append(output)
                input = range(min(interval.stop, input.stop), input.stop)
                print('Generated output {}. New input {}'.format(output, input))
            elif interval.start in input:
                output = range(interval.start + offset, min(interval.stop, input.stop) + offset)
                y.append(output)
                input0 = range(min(interval.stop, input.stop), input.stop)
                x.append(input0)
                input = range(input.start, interval.start)
                print('Generated output {}. New inputs are {} and {}'.format(output, input, input0))
        if len(input)!=0: y.append(input)
        #y=set(y)
        #y=[item for item in y]
    print('Map output is {} intervals: {}'.format(len(y), y))
    x = y

locations = [ranges.start for ranges in y]



                #i = i+1
                #statement = '{} is in {}: {}'
                #print(statement.format(x, range[0], (x in range[0])))
                #if x in intervals[0]: y = x+k
            #print('y is '+str(y))
            #x = y
        #locations.append(y)

#print(locations)
print('Minimum over all locations is {}'.format(min(locations)))

#for some reason my solution is still not right.
#I could still try object oriented programming - making use of classes for seeds, soil etc, defining the maps for them
# I could try to use numpy to make it work maybe in a less excruciating way. maybe my code will get cleaner and it will become more apparent where mistakes might be hiding.
# I could think more about edge cases.
# I could go to reddit and see how others have solved it.