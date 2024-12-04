number = [1,2,3]
new_number =[ n +1 for n in number]
print(new_number)

name = "sunil"
letter_list = [letter for letter in name]
print(letter_list)

number_list = [number * 2  for number in  range(1, 5)]
print(number_list)


name_list = ["sunil", "shanaya", "shantanu", "rupam", "ishu", "lisa"]
names = [n for n in name_list if len(n) < 5]
print(names)

names_list = [n.upper() for n in name_list if len(n) > 5]
print(names_list)


