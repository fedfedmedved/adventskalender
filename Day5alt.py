import re
import numpy as np

read_data = open('day5test.txt').read().split('\n\n') #split file at empty lines
read_data = [item.splitlines() for item in read_data]

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

data = []
data.append( re.findall('\d+', read_data[0][0]) ) #seeds
print(data[0])

for maps in read_data[1:]:
    for line in maps[1:]:
        line = [int(number) for number in line.split(' ')]
        line = range(line[1], line[1] + line[2]), line[0] - line[1]
        def
print(read_data)
print(type(data[0]))

#seed2soil = lambda x: