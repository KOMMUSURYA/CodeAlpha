def input_grades():
    grades = {}
    
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        grade = float(input(f"Enter the grade for {subject}: "))
        grades[subject] = grade
    
    return grades

def calculate_average(grades):
    if grades:
        return sum(grades.values()) / len(grades)
    return  

def display_grades(grades):
    print("\nGrades:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    avg = calculate_average(grades)
    print(f"\nAverage Grade: {avg:.2f}")

def main():
    print("Welcome to the Student Grade Tracker!")
    grades = input_grades()
    display_grades(grades)

if __name__ == "__main__":
    main()
