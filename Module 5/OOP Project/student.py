import Grade as g

class Student:
    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name

        self.course_registered = {}

    def register_course(self, course_manager):
        # TODO: Implement Course Manager class
        course_manager.get_courses()
        option = input()
        # TODO: Implement logic for schedule conflict

        # TODO: Implement Grade Class
        grade_obj = g.Grade(self, course_manager.course_list[option])

        course_manager.course_list[option].decrease_seat()

        self.course_registered[course_manager.course_list[option]] = grade_obj 

    def print_schedule(self):
        for course in self.course_registered:
            print(f"{course.name} - {course.date} - {course.time}")
    
    def view_grades(self):
        for course in self.course_registered:
            print(f"{course.name} - {self.course_registered[course].grade}")