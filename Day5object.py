import re
import numpy as np

data = open('day5.txt').read().split('\n\n') #split file at empty lines
data = [item.splitlines() for item in data]

#i'd probably like to define a set of functions that preform all the appropriate conversions for me.

#first we'll process the seeds into seeds and ranges (as per part 2)

data_pt2 = [range( int(seeds), int(seeds)+int(ranges) ) for seeds, ranges in re.findall('(?P<seeds>\d+)(?:\ )(?P<ranges>\d+)', data[0][0])]

# our maps are actually functions y = x + s, where s is a step function
# here we are repackaging maps into domain intervals and values of offset k.

#### Part 1
data_pt1 = [int(seeds) for seeds in re.findall('\d+', data[0][0])] #seeds pt1

#### this is the core that i will have to change. first, i want to make objects out of 'seeds', or out of maps.
# then i'll either define bunch of maps, or what?
# for partwo i was thinking of splitting and offsetting intervals. an object (interval) can be split into two new objects.
# i also want to offset self. could do that with a function, no se.

# class Seeds:
#     def __init__(self, number):
#         self.value = number
#     def transfm:
#         if self.value in

class constant_offset_map: #linear map of type y = x + k
    def __init__(self, params):
        y,x,length = params #unpacking params (they are packed in a numpy array of ints)
        self.domain = range(x, x + length)
        self.offset = y-x #k
    def apply_step(self, array):
        #vectorized
        # i need for at most one step to be applied to each input. could just add up offsets
        return (array >= self.domain.start) * (array < self.domain.stop) * self.offset

class maps:
    def __init__(self, name, data):
        data = [np.array(line.split(' '), dtype=int) for line in data] #see no reason to use 'real' vectorization here
        self.Inhalt = [constant_offset_map(input) for input in data] #creating instances of offset maps
        self.name = name
    def apply_map(map, number):
        print(map.name)
        total_offset = number*0
        for step in map.Inhalt:
            total_offset = total_offset + step.apply_step(number)
        number = number + total_offset
        print(number)
        return number

map_objects = [] #populating maps with objects
for map in data[1:]:
    map_instance = maps(map[0], map[1:]) #creating instance of class
    map_objects.append(map_instance)

x = np.array(data_pt1)

for map in map_objects:
    x = map.apply_map(x)
print(x)
print(x.min())

#### Part 2 Solution

# print(data)
#
#
# x = data[0] #take seed ranges as function input
# for map in data[1:]:
#     y=[]
#     print(map[0])
#     #y = x
#     #pass in ranges that were outputs from previous maps
#     #alternatively, take all ranges (not a set, repeated elements are allowed) and one input range
#     # sort points lowest to highest, keeping track of start and end. now, look left of input.start. is it a start?
#     for input in x:
#         for interval, offset in map[1:]:
#             if input.start in interval:
#                 output = range(input.start + offset, min(interval.stop, input.stop) + offset)
#                 y.append(output)
#                 input = range(min(interval.stop, input.stop), input.stop)
#                 print('Generated output {}. New input {}'.format(output, input))
#             elif interval.start in input:
#                 output = range(interval.start + offset, min(interval.stop, input.stop) + offset)
#                 y.append(output)
#                 input0 = range(min(interval.stop, input.stop), input.stop)
#                 x.append(input0)
#                 input = range(input.start, interval.start)
#                 print('Generated output {}. New inputs are {} and {}'.format(output, input, input0))
#         if len(input)!=0: y.append(input)
#         #y=set(y)
#         #y=[item for item in y]
#     print('Map output is {} intervals: {}'.format(len(y), y))
#     x = y

# locations = [ranges.start for ranges in y]



                #i = i+1
                #statement = '{} is in {}: {}'
                #print(statement.format(x, range[0], (x in range[0])))
                #if x in intervals[0]: y = x+k
            #print('y is '+str(y))
            #x = y
        #locations.append(y)

#print(locations)
# print('Minimum over all locations is {}'.format(min(locations)))

#for some reason my solution is still not right.
#I could still try object oriented programming - making use of classes for seeds, soil etc, defining the maps for them
# I could try to use numpy to make it work maybe in a less excruciating way. maybe my code will get cleaner and it will become more apparent where mistakes might be hiding.
# I could think more about edge cases.
# I could go to reddit and see how others have solved it.