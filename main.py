names = ["sunil", "shanaya", "Shantanu", "Suman", "SKSUMAN"]

import random

student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

passed_student = {student:score for (student, score) in student_score.items() if score > 60}
print(passed_student)

#Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_word = sentence.split()
words = {word for word in split_word}
print(words)
result = {w : len(w) for w  in words}
print(result)
print(result.items())
cn = {e for (c,e) in result.items()}
print(cn)
#Dictionary Comprehension 2

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
temp_c = {day:(temp * 9/5)+32 for (day , temp) in weather_c.items()}
print(temp_c)




