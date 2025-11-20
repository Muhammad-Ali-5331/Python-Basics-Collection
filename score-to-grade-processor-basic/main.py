student_scores = {
    "Ali" : 81,
    "Ahmed" : 78,
    "Umer" : 68,
    "Shehbaz" : 74,
    "Faizan" : 52,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for i in student_grades:
    print(f"\n{i}: {student_grades[i]}")