import os
import matplotlib.pyplot as plt


def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file]


def get_student_grade(students, assignments, submissions, student_name):
    student = next((s for s in students if s[1] == student_name), None)
    if not student:
        return "Student not found"
    student_id = student[0]
    total_score = sum(
        float(sub[2]) * int(assignment[1]) / 100
        for sub in submissions if sub[0] == student_id
        for assignment in assignments if assignment[0] == sub[1]
    )
    return f"{round((total_score / 1000) * 100)}%"


def get_assignment_stats(assignments, submissions, assignment_name):
    assignment = next((a for a in assignments if a[1] == assignment_name), None)
    if not assignment:
        return "Assignment not found"
    assignment_id = assignment[0]
    scores = [float(sub[2]) for sub in submissions if sub[1] == assignment_id]
    return f"Min: {min(scores)}%, Avg: {sum(scores) / len(scores):.2f}%, Max: {max(scores)}%"


def display_histogram(assignments, submissions, assignment_name):
    assignment = next((a for a in assignments if a[1] == assignment_name), None)
    if not assignment:
        print("Assignment not found")
        return
    assignment_id = assignment[0]
    scores = [float(sub[2]) for sub in submissions if sub[1] == assignment_id]
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(f"Histogram for {assignment_name}")
    plt.xlabel("Score Ranges")
    plt.ylabel("Frequency")
    plt.show()


def main():
    students = load_data('data/students.txt')
    assignments = load_data('data/assignments.txt')
    submissions = load_data('data/submissions.txt')

    while True:
        print("\n1. Student grade\n2. Assignment statistics\n3. Assignment graph\n")
        selection = input("Enter your selection: ")
        if selection == "1":
            student_name = input("What is the student's name: ")
            print(get_student_grade(students, assignments, submissions, student_name))
        elif selection == "2":
            assignment_name = input("What is the assignment name: ")
            print(get_assignment_stats(assignments, submissions, assignment_name))
        elif selection == "3":
            assignment_name = input("What is the assignment name: ")
            display_histogram(assignments, submissions, assignment_name)
        else:
            print("Invalid selection. Exiting.")
            break


if __name__ == "__main__":
    main()
