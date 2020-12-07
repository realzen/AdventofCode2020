file = open("/home/ernesto/Desktop/AdventofCode2020/Day05/day05_input.txt")
file = file.readlines()

print(file)

# list =- []
# for i in file:
#     row_upper= 128
#     row_lower= 0
#     final_row = 0
#     col = 8
#     col_upper = 7
#     col_lower = 0
#     final_col = 0
#     for n in range(len(i)):
#         print("THIS IS N:", n)
#         if n < 7:
#             print("These are the first seven characters:", i[n])
#             if n == "F":
#                 row_upper = if row_lower != 0 row_upper - (row_lower / 2) else (row_upper / 2) - 1
#                 if n == 6:
#                     final_row = row_upper
#             if n == "B":
#                 row_lower = if row_lower != 0 row_upper - (row_lower / 2) + 1 else (row_upper / 2) + 1
#                 if n == 6:
#                     final_row = row_lower
                
#         if n > 7 and n < 10:
#             print("These are the next 3:", i[n])
#             col = col / 2
#             if n == "R":
#                 col_lower = col_lower + col
#                 if n == 9:
#                     final_col = col_upper
#             if n == "L":
#                 col_upper = col_upper - col
#                 if n == 9:
#                     final_col = col_lower       
#         print("This is the row:", final_row)
#         print("This is the column", final_col)

theList = "FBFBBFFRLR"
row = 128
row_upper= 127
row_lower= 0
final_row = 0
col = 8
col_upper = 7
col_lower = 0
final_col = 0
for n in range(len(theList)):
        print ("index:", n)
        if n < 7:
            print("CHAR:", theList[n])
            row = row / 2
            print(">>>>INDEX:", row_lower, ", ", row_upper)
            if theList[n] == "F":
                print("[F]")
                print(row_upper,"-", row)
                row_upper = row_upper - row
                if n == 6:
                    final_row = row_upper
            if theList[n] == "B":
                print("[B]")
                print(row_lower,"+", row)
                row_lower = row_lower + row
                if n == 6:
                    final_row = row_lower
                
        if n >= 7 and n < 10:
            print("____________________________________")
            print("CHAR:", theList[n])
            col = col / 2
            print(">>>>INDEX:", col_lower, ", ", col_upper)
            if theList[n] == "R":
                print(col_lower,"+", col)
                col_lower = col_lower + col
                if n == 9:
                    final_col = col_upper
            if theList[n] == "L":
                print(col_upper,"-", col)
                col_upper = col_upper - col
                if n == 9:
                    final_col = col       

print("This is the row:", final_row)
print("This is the column", final_col)