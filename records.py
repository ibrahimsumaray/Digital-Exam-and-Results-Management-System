"""records.py - Storage functions.

ONE data structure is used: a dictionary.
Key   = tuple (student_id, exam_code)  -> unique per result
Value = Result object
"""


def add_record(records, result):
    """Add a Result to the dictionary. Returns True if added."""
    key = (result.student.student_id, result.exam.exam_code)
    if key in records:
        print("  ! A result for this student and exam already exists.")
        return False
    records[key] = result
    return True


def display_records(records):
    """Display every stored result."""
    if not records:
        print("  (No records yet)")
        return
    print(f"{'STUDENT':<8} | {'EXAM':<6} | {'SUBJECT':<12} | "
          f"{'SCORE':<7} | {'PERCENT':<6} | GRADE   | STATUS")
    print("-" * 78)
    for result in records.values():
        result.display_info()


def find_record(records, student_id, exam_code):
    """Return a Result or None."""
    return records.get((student_id, exam_code))


def find_student(records, student_id):
    """Return an existing Student object (or None)."""
    for result in records.values():
        if result.student.student_id == student_id:
            return result.student
    return None


def find_exam(records, exam_code):
    """Return an existing Exam object (or None)."""
    for result in records.values():
        if result.exam.exam_code == exam_code:
            return result.exam
    return None


def class_average(records, exam_code):
    """Average percentage for one exam, or None if no results."""
    total = 0
    count = 0
    for result in records.values():
        if result.exam.exam_code == exam_code:
            total += result.percentage()
            count += 1
    return total / count if count else None
