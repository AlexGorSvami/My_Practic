# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
# peter = Character()
# peter.name = 'Peter'
# peter.last_name = 'Parker'
# peter.age = 26
# peter.job = 'photographer'
# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)

# peter.name = 'Peter Parker'
# peter.power = 70
# peter.alias = 'Spider-men'
# print(peter.alias)
# print(peter.__dict__)
#
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
# bruce.alias = 'Batman'
# print(bruce.__dict__)

# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#
#     def eat(self,food):
#         if self.energy < 100:
#             self.enegry += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self,hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self,new_alias):
#         print(self)
#         self.alias = new_alias
#
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
# print(bruce.alias)
# bruce.change_alias('Batman')
# print(bruce.alias)
# bruce.change_alias('Dark Knight')
# print(bruce.alias)
#
# bruce.do_exercise(1)
# print(bruce.power)
# print(bruce.energy)
# bruce.do_exercise(2)
# print(bruce.power)
# print(bruce.energy)
# bruce.do_exercise(2)
# print(bruce.power)
# print(bruce.energy)
#
# class Character:
#     name = ''
#     power = 0
#     energy = 0
#     hands = 2
#     backpack = []
#
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         self.alias = new_alias
#
# peter = Character()
# bruce = Character()
#
# peter.backpack.append('wed-shooters')
# print(peter.backpack)
# print(bruce.backpack)

# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.enegry = energy
#         self.backpack = []
#         self.hands = hands
#
#     def eat(self, food):
#         if self.enegry < 100:
#             self.enegry += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self,hours):
#         if self.enegry > 0:
#             self.enegry -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         self.alias = new_alias
#
#     def beat_up(self, foe):
#
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
# peter = Character('Peter Parker', 80)
# bruce = Character('Bruce Wayne', 85)
#
# print(peter.name)
# print(peter.power)
# print(peter.__dict__)
#
# peter.backpack.append('web-shooters')
#
# print(peter.backpack)
# print(bruce.backpack)
#
# bruce.beat_up(peter)
# print(peter.status)
# print(bruce.status)
# peter.beat_up(bruce)


# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.finished_courses_in_progress = []
#         self.grades = {}
#
# class Mentor:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.finished_courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
#
# print(best_student.finished_courses)
# print(best_student.finished_courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)
#

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def add_courses(self, course_name):
#         self.finished_course.append(course_name)
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

# ---------------------Lection 2-------------------

# class Character:
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = []
#         self.hands = hands
#
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         self.alias = new_alias
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
#
# peter = Character('Peter Parker', 80)
# peter.change_alias('Spidar-Man')
# print(peter.backpack)
# print(peter.alias)
# peter.do_exercise(5)


# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#
#
#
#
#
# class Spider:
#     power = 0
#     energy = 50
#     hands = 8
#
#     def wedshoot(self):
#         print('Pew-Pew!')
#
# class SpiderMan(Character, Spider):
#     pass
#
#
# peter_parker = SpiderMan()
# print(peter_parker.name)
# print(peter_parker.power)
# print(peter_parker.energy)
# print(peter_parker.hands)
# peter_parker.wedshoot()
#
# print(SpiderMan.mro())


