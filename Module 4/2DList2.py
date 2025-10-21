def avg(grading_item_list):
    sum = 0

    for item in grading_item_list:
        sum += item
    
    return sum / len(grading_item_list)

def calc_final_grade(lab, assignment, midterm, final):
    return lab * 0.1 + assignment * 0.4 + midterm * 0.2 + final * 0.3

def main():
    student_list = [
        ["John", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
        ["Alice", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
        ["Bob", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
        ["Charlie", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
    ]

    for student in student_list:
        name = student[0]
        lab = avg(student[1:14])
        assignment = avg(student[14:21])
        midterm_exam = student[21]
        final_exam = student[22]
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



    

if __name__ == "__main__":
    main()