class Student:
  def __init__(self, name, roll_number, love):
    self.name = name
    self.roll_number = roll_number
    self.love = love

def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student: student.love, reverse=True)
  return sorted_students

students = [
Student("AADHI", "A123", 9.8),
Student("LATHIF", "A124", 8.7),
Student ("DINESH", "A125", 7.6), Student ("PRASANTH", "A126", 6.5),]

sorted_students = sort_students (students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, LOVE: {}".format(student.name,student.roll_number,student.love))