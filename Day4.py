import re
import numpy as np

data = open('day4.txt').read().splitlines()
total_points = 0
i=0
card_copies = np.ones(len(data))

while i!=len(data):
    #take winning lottery numbers and elf's numbers from the 0'th lottery ticket
    winning_numbers = data[i].split(':')[1].split('|')[0].strip()
    elf_numbers = data[i].split(':')[1].split('|')[1].strip()

    #make strings into sets of numbers
    winning_numbers = re.findall('\d+',winning_numbers)
    winning_numbers = set([int(numbers) for numbers in winning_numbers])

    elf_numbers = re.findall('\d+',elf_numbers)
    elf_numbers = set([int(numbers) for numbers in elf_numbers])
    wins = len(elf_numbers.intersection(winning_numbers))
    if wins>0:
        card_value=2**(wins-1)
        total_points = total_points + card_value
        card_copies[(i+1):(i+wins+1)] = card_copies[(i+1):(i+wins+1)] + 1*card_copies[i]
        #increase copies by 1 for the next k cards, where k is #wins
    i = i+1


print(card_copies.sum())