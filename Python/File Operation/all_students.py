fr_all_students = open("Python\\File Operation\\all_students.txt")
fr_paased_students = open("Python\\File Operation\\passed_students.txt")
fw_failed_students = open("Python\\File Operation\\failed_students.txt", "w")

all_students = {name.rstrip("\n") for name in fr_all_students}
passed_students = {name.rstrip("\n") for name in fr_paased_students}

failed_students = all_students.difference(passed_students)

for student in failed_students:
    fw_failed_students.write(student + "\n")

