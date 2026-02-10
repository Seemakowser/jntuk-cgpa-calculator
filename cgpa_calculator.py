GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0
}

def calculate_sgpa():
    subjects = int(input("Enter number of subjects: "))

    total_credits = 0.0
    total_points = 0.0
    failed = False

    for i in range(subjects):
        print(f"\nSubject {i+1}")
        credits = float(input("Enter credits (can be decimal): "))
        grade = input("Enter grade (S/A/B/C/D/E/F): ").upper()

        if grade not in GRADE_POINTS:
            print("Invalid grade entered.")
            return None, None, None

        if grade == "F":
            failed = True

        grade_point = GRADE_POINTS[grade]
        total_credits += credits
        total_points += credits * grade_point

    sgpa = total_points / total_credits
    return sgpa, total_credits, failed

def calculate_cgpa():
    semesters = int(input("Enter number of semesters: "))

    overall_points = 0.0
    overall_credits = 0.0

    for sem in range(semesters):
        print(f"\n--- Semester {sem+1} ---")
        sgpa, credits, failed = calculate_sgpa()

        if sgpa is None:
            return

        if failed:
            print("⚠️ Student has failed in one or more subjects.")

        print(f"SGPA of Semester {sem+1}: {sgpa:.2f}")

        overall_points += sgpa * credits
        overall_credits += credits

    cgpa = overall_points / overall_credits
    print(f"\n🎓 Final CGPA: {cgpa:.2f}")

def main():
    print("JNTUK CGPA Calculator")
    calculate_cgpa()

if __name__ == "__main__":
    main()
