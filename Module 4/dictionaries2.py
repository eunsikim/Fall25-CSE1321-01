def avg(grading_item_list):
    sum = 0

    for item in grading_item_list:
        sum += item
    
    return sum / len(grading_item_list)

def calc_final_grade(lab, assignment, midterm, final):
    return lab * 0.1 + assignment * 0.4 + midterm * 0.2 + final * 0.3

def main():
    student_dictionary = {
        # KEY:[0]Labs, [1]Assignments, [2]Midterm, [3]Final Exam
        "John":[
            #Labs
            [80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89],
            #Assignments
            [90, 100, 80, 81, 90, 100, 78],
            #Midterm 
            90, 
            #Final Exam
            91
        ]
    }

    for student in student_dictionary:
        name = student
        lab = avg(student_dictionary[student][0])
        assignment = avg(student_dictionary[student][1])
        midterm_exam = student_dictionary[student][2]
        final_exam = student_dictionary[student][3]
        final_grade = calc_final_grade(lab, assignment, midterm_exam, final_exam)

        print(f"Student: {name}, final grade: {final_grade}")

    # Alternative approach where we want to skip the first student (start at index 1)
    # for i in range(1, len(student_list)):
    #     name = student_list[i][0]
    #     lab = avg(student_list[i][1:14])
    #     assignment = avg(student_list[i][14:21])
    #     midterm_exam = student_list[i][21]
    #     final_exam = student_list[i][22]
    #     final_grade = calc_final_grade(lab, assignment, midterm_exam, final_exam)

    #     print(f"Student: {name}, final grade: {final_grade}")

    print(student_dictionary["John"])

    

if __name__ == "__main__":
    main()