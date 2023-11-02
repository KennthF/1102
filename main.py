
#with open("three_digit_numbers.txt", "r") as file_num:
 #   file_content = file_num.read()

#file_content = "380 339 420 308 448"

cols = file_content.split(" ")

list_num = []

for i in cols:
    num = int(i)
    list_num.append(num)

for count in range (min(list_num), max(list_num) + 1):
    if count not in list_num:
        print(f"{count} is missing")

    else:
        print(f"\n{count} is not missing\n")

