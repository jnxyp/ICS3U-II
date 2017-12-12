# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-01
# Loops, Lists and Functions - Question 2


def scale_midterm_grades(grades, multiplier, bonus):
    i = 0
    while i < len(grades):
        grades[i] = round(grades[i] * multiplier + bonus, 1)
        if grades[i] > 100:
            grades[i] = 100
        i += 1


grades = [45, 50, 55, 95]
scale_midterm_grades(grades, 1.1, 10)
print(grades)
