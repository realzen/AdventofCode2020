import re
file = open"../AdventofCode2020/Day04/day04_input.txt")
file = file.readlines()


lines = []
counter = 0
lines.append("")
for i in file:
    if i == '\n':
        counter +=1
        lines.append("")
    else:
        new_line = i.replace('\n',' ')
        lines[counter] = lines[counter] + new_line
        
values = ["ecl","pid", "eyr", "hcl", "byr", "iyr", "hgt"]
valid_count = 0
validation = 0
for i in lines:
    if all(k in i for k in values):
        valid_count += 1
        List = i.split()
        ecl,pid,eyr,hcl,byr,iyr,hgt = False,False,False,False,False,False,False
        for k in List:
            field,value = k.split(":")
            eye_color = "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
            if field == "byr" and len(value) == 4 and (1920 <= int(value) <= 2002):
                byr = True
            if field == "iyr" and len(value) == 4 and (2010 <= int(value) <= 2020):
                iyr = True
            if field == "eyr" and len(value) == 4 and (2020 <= int(value) <= 2030):
                eyr = True
            if field == "hgt" and re.search("^\d+[cm]|[in]",value):
                numbers = re.search("\d+",value)
                numbers = numbers.group(0)
                if (value.find("cm") != -1 and 150 <= int(numbers) <= 193) or (value.find("in") != -1 and 59 <= int(numbers) <= 76):
                    hgt = True
            if field == "hcl" and len(value) == 7 and re.search("^#([0-9]|[a-f])", value):
                hcl = True
            if field == "ecl" and (len(value) == 3) and value in eye_color:
                ecl = True
            if field == "pid" and (len(value) == 9) and re.search("[0-9]", value):
                pid = True
        if ecl and pid and eyr and hcl and byr and iyr and hgt:
            validation += 1
print("Answer 1:", valid_count)
print("Answer 2:", validation)
