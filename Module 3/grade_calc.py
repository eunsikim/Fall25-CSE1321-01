def calc_avg(sum_items, num_items):
    return sum_items / num_items

def calc_weight(avg_items, weight_item):
    return avg_items * weight_item

def calc_grade(checkMax, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2):
    if checkMax:
        unknown_labs = 800
        unknown_assignments = 500
        unknown_midterm = 100
        unknown_final = 100
    else:
        unknown_labs = 0
        unknown_assignments = 0
        unknown_midterm = 0
        unknown_final = 0

    labs = calc_weight(calc_avg(lab1 + lab2 + lab3 + lab4 + lab5 + unknown_labs, 13), 0.1)
    assignments = calc_weight(calc_avg(assignment1 + assignment2 + unknown_assignments, 7), 0.4)
    midterm_exam = calc_weight(unknown_midterm, 0.2)
    final_exam = calc_weight(unknown_final, 0.3)
    final_grade = labs + assignments + midterm_exam + final_exam
    
    return final_grade
    
# 13 Labs (10%), 7 Assignments (40%), Midterm (20%), Final (30%).
# We are not implementing policy.
def main():
    lab1 = float(input("Enter value for lab 1: "))
    lab2 = float(input("Enter value for lab 2: "))
    lab3 = float(input("Enter value for lab 3: "))
    lab4 = float(input("Enter value for lab 4: "))
    lab5 = float(input("Enter value for lab 5: "))

    assignment1 = float(input("Enter value for assignment 1: "))
    assignment2 = float(input("Enter value for assignment 2: "))

    final_grade_max = calc_grade(True, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2)
    print(f"Maximum possible grade: {final_grade_max:.2f}")


    final_grade_min = calc_grade(False, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2)
    print(f"Minimum possible grade: {final_grade_min:.2f}")


if __name__ == "__main__":
    main()