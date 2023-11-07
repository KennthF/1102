with open("three_digit_numbers.txt", "r") as file:
    content = file.read()
    content = content.replace("\n"," ") #Removes the line space
    content = content.split(" ") #Split by spaces
    
      

values = []

for i in content:
    if i.isnumeric(): #Turn it into a number
        values.append(int(i))

print(values)

print("\n")

print(content)


 
    