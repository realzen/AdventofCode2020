# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
# 
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
# 
# To save your vacation, you need to get all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
# 
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# 
# For example, suppose your expense report contained the following:
# 
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
# 
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

print("Running.....")
file1 = open('/Users/ernestovaldez/Desktop/github/AdventofCode2020/Day05/day05_input.txt', 'r') 
Lines = file1.readlines()
count = 0
d = {}
# read file into dictionary
for line in Lines:
    count += 1
    # print("Line {}: {}".format(count,line.strip())) 
    (key, value) = line,count
    d[int(key)] = value

# search through dictionary and find answer
for val in d:
    x = 2020 - val
    if d.get(x):
        print('First Answer : ', val * x)
        break


# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
# 
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
# 
# In your expense report, what is the product of the three entries that sum to 2020?

# create a sorted list
sorted_list = list(sorted(d.keys()))
for i in sorted_list:
    found = False
    for k in reversed(sorted_list):
        x = (2020 - i) - k
        if d.get(x) and k != i:
            found = True
            break
    if found:
        prod = x * i * k
        print("Second answer : ", prod)
        break