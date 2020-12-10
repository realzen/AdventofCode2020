file = open("../AdventofCode2020/Day06/day06_input.txt")
file = file.readlines()

sum_answers = 0
counter = 0
groups = []
group_string = ""
for i in file:
    group_string = group_string + i.rstrip()
    if i == "\n":
        groups.append(group_string)
        group_string = ""
        
groups.append(group_string) #for the last line

for i in groups:
    counter += 1
    # print(counter, ":", i)
    group_sum = 0
    alphabet = 97
    for k in range(97,123):
        # print("This is the character", k, "This is the Letter", chr(k))
        if (i.find(chr(k))) != -1:
            group_sum += 1
    sum_answers += group_sum

print("Answer 1:", sum_answers)
    