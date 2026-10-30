"""models.py - Core classes for the Digital Exam & Results Management System.

Privacy note (DPG): students are identified ONLY by an anonymous ID
(e.g. STU-001). No names, addresses, phone numbers or other personal data.
"""

# Tuple (immutable) of grade boundaries: (minimum percentage, grade letter)
GRADE_BOUNDARIES = (
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
)


class Student:
    """A student identified by an anonymous ID only."""

    _counter = 0  # class attribute: used to generate anonymous IDs

    def __init__(self, student_id, level):
        self.student_id = student_id
        self.level = level  # e.g. "Year 1"

    # ---- class method: alternative constructor ----
    @classmethod
    def create_anonymous(cls, level):
        """Create a student with an auto-generated anonymous ID."""
        cls._counter += 1
        return cls(f"STU-{cls._counter:03d}", level)

    # ---- static method: utility not needing self/cls ----
    @staticmethod
    def is_valid_id(student_id):
        """A valid ID looks like STU-001."""
        return (
            len(student_id) == 7
            and student_id.startswith("STU-")
            and student_id[4:].isdigit()
        )

    # ---- instance method ----
    def display_info(self):
        print(f"Student ID: {self.student_id} | Level: {self.level}")


class Exam:
    """An exam with a subject, a maximum score and a pass mark."""

    def __init__(self, exam_code, subject, max_score, pass_mark):
        self.exam_code = exam_code
        self.subject = subject
        self.max_score = max_score
        self.pass_mark = pass_mark

    # ---- class method: build an Exam from text "E101,Maths,100,50" ----
    @classmethod
    def from_string(cls, text):
        code, subject, max_score, pass_mark = text.split(",")
        return cls(code.strip(), subject.strip(),
                   int(max_score), int(pass_mark))

    # ---- instance methods ----
    def is_valid_score(self, score):
        return 0 <= score <= self.max_score

    def display_info(self):
        print(f"Exam: {self.exam_code} | Subject: {self.subject} | "
              f"Max: {self.max_score} | Pass mark: {self.pass_mark}")


class Result:
    """Links ONE Student to ONE Exam with a score (object interaction)."""

    def __init__(self, student, exam, score):
        if not exam.is_valid_score(score):
            raise ValueError(
                f"Score must be between 0 and {exam.max_score}.")
        self.student = student   # Student object
        self.exam = exam         # Exam object
        self.score = score

    # ---- static method: grade from percentage using the tuple ----
    @staticmethod
    def calculate_grade(percentage):
        for minimum, letter in GRADE_BOUNDARIES:
            if percentage >= minimum:
                return letter
        return "F"

    # ---- instance methods ----
    def percentage(self):
        return (self.score / self.exam.max_score) * 100

    def grade(self):
        return Result.calculate_grade(self.percentage())

    def status(self):
        return "PASS" if self.score >= self.exam.pass_mark else "FAIL"

    def update_record(self, new_score):
        """Correct a score (validated against the exam's maximum)."""
        if not self.exam.is_valid_score(new_score):
            raise ValueError(
                f"Score must be between 0 and {self.exam.max_score}.")
        self.score = new_score

    def display_info(self):
        print(f"{self.student.student_id:<8} | {self.exam.exam_code:<6} | "
              f"{self.exam.subject:<12} | {self.score:>3}/"
              f"{self.exam.max_score:<3} | {self.percentage():>5.1f}% | "
              f"Grade {self.grade()} | {self.status()}")
