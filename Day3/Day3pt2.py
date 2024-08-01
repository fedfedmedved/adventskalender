import re
import numpy as np

data = open('day3.txt').read().splitlines()

# using finditer i get match objects, which include what i match as well as spans. spans will be crucial for this task.

# in my schematic two matched objects are adjacent if their lines are adjacent and if their spans are adjacent.

# if i wanted to do this elegantly, i would first finditer all symbols, then save their spans as a numpy array. i would then like to expand their spans by 1 in each direction. so, if i have a match at position (1,3) i would like to expand the range to a slice (0:3, 2:5). that would be very visual and enjoyable, but it looks like work.


# numbers = [match for match in re.finditer('\d+',data[0])] #finditer creates a list of match objects

numbers = [[match for match in re.finditer('\d+',line)] for line in data] #matching all numbers
symbols = [[match for match in re.finditer('[^.|\d]',line)] for line in data] #matching symbols
stars = [[match for match in re.finditer('\*',line)] for line in data] #matching all numbers

# len(symbols) == len(numbers) == len(data) #checking that lengths match

#my_span = numbers[0][0].span()
#my_span = range(my_span[0]-1, my_span[1]+1) #expanded the range by 1 to include adjacency
#position = symbols[1][0].span()[0]

# now that i have a good test for adjacency i just have to make sure to check all possible adjacencies between the lines, also for several symbols in one line

# first let's check whether a given number has an adjacent symbol:

# need to not forget to treat empty lists correctly

adjacency = False
gear_adj = 0
gears=[]
sum_parts = 0
sum_ratios = 0
i=0 #is my line indicator
while i !=len(data):
    gears.append([])
    for s in stars[i]:
        gear_adj = 0
        gear_matches = []
        for k in range(max(0, i-1), min(i+2, len(data))): #check lines above and below a star
            for m in numbers[k]:
                m_span = range(m.span()[0], m.span()[1])
                window = range(s.span()[0]-1, s.span()[1]+1) #search window around the star
                window = set(window) #making it into a set, so i can intersect
                intersect = window.intersection(m_span)
                if (len(intersect)>0):
                    gear_adj = gear_adj+1
                    gear_matches.append(int(m[0]))
        if (gear_adj == 2):
            gears[i].append(s)
            gear_matches = np.array(gear_matches)
            gear_ratio = gear_matches.prod()
            sum_ratios = sum_ratios + gear_ratio
            #sum_parts = sum_parts + int(m[0])
    i = i+1

print(sum_ratios)


