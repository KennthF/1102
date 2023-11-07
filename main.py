with open("three_digit_numbers.txt", "r") as file:
    content = file.read()
    content = content.replace("\n"," ") #Removes the line space
    content = content.split(" ") #Split by spaces
    
      

values = []

for i in content:
    if i.isnumeric(): #Turn it into a number
        values.append(int(i))

new_file = open("sorted_numbers.txt", "w") #Write a new file

#Sort the file and get the missing number
for i in range(min(values), max(values) + 1):
    if i in values:
        new_file.write(f"{i} is not missing.\n")

    else:
        new_file.write(f"{i} is missing.\n")

new_file.close()

with open("sorted_numbers.txt", "r") as sorted_file:
    print(sorted_file.read())


 
    