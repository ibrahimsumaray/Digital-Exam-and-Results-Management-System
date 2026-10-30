"""main.py - Digital Exam & Results Management System (menu program)."""

from models import Student, Exam, Result
from records import (add_record, display_records, find_record,
                     find_student, find_exam, class_average)


def read_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Please type a whole number.")


def load_demo_data(records):
    """Create sample objects and show how they interact."""
    maths = Exam.from_string("E101, Mathematics, 100, 50")   # class method
    english = Exam.from_string("E102, English, 100, 50")
    s1 = Student.create_anonymous("Year 1")                  # class method
    s2 = Student.create_anonymous("Year 1")
    s3 = Student.create_anonymous("Year 2")
    demo = (
        (s1, maths, 85), (s2, maths, 62), (s3, maths, 41),
        (s1, english, 74), (s2, english, 55),
    )
    for student, exam, score in demo:
        add_record(records, Result(student, exam, score))
    print("  Demo data loaded.")


def add_result_menu(records):
    level = input("  Student level (e.g. Year 1): ").strip() or "Year 1"
    sid = input("  Student ID (e.g. STU-001, or press Enter for new): ").strip()
    if sid == "":
        student = Student.create_anonymous(level)
        print(f"  New anonymous ID created: {student.student_id}")
    elif not Student.is_valid_id(sid):                       # static method
        print("  ! Invalid ID. Use the format STU-001.")
        return
    else:
        student = find_student(records, sid) or Student(sid, level)

    code = input("  Exam code (e.g. E101): ").strip().upper()
    exam = find_exam(records, code)
    if exam is None:
        text = input("  New exam. Enter 'code,subject,max,passmark' "
                     "(e.g. E103,Science,100,50): ")
        try:
            exam = Exam.from_string(text)
        except ValueError:
            print("  ! Wrong format. Exam not created.")
            return
    score = read_int("  Score: ")
    try:
        result = Result(student, exam, score)
    except ValueError as error:
        print(f"  ! {error}")
        return
    if add_record(records, result):
        print("  Result saved.")
        result.display_info()


def update_menu(records):
    sid = input("  Student ID: ").strip()
    code = input("  Exam code: ").strip().upper()
    result = find_record(records, sid, code)
    if result is None:
        print("  ! Record not found.")
        return
    new_score = read_int("  New score: ")
    try:
        result.update_record(new_score)
        print("  Updated:")
        result.display_info()
    except ValueError as error:
        print(f"  ! {error}")


def average_menu(records):
    code = input("  Exam code: ").strip().upper()
    avg = class_average(records, code)
    if avg is None:
        print("  ! No results for that exam.")
    else:
        print(f"  Average for {code}: {avg:.1f}%")


def main():
    records = {}   # the ONE data structure: dictionary
    print("=" * 50)
    print(" DIGITAL EXAM & RESULTS MANAGEMENT SYSTEM")
    print(" (anonymous IDs only - no personal data stored)")
    print("=" * 50)
    while True:
        print("\n1. Load demo data")
        print("2. Add a result")
        print("3. Display all results")
        print("4. Update a score")
        print("5. Show exam average")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            load_demo_data(records)
        elif choice == "2":
            add_result_menu(records)
        elif choice == "3":
            display_records(records)
        elif choice == "4":
            update_menu(records)
        elif choice == "5":
            average_menu(records)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
