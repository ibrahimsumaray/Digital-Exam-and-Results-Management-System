# Digital Exam & Results Management System

**Module:** PROG211 Object-Oriented Programming 1 (Individual Assignment)
**Domain:** Education
**Language:** Python 3 (no external libraries)

## Problem Solved
Schools often record exam results on paper, which causes lost records, slow
grading and calculation mistakes. This program records exam scores, calculates
percentages and grades automatically, allows corrections, and shows class averages.

## How to Run
```
python main.py
```
Choose **1** to load demo data, then try the other options.

## Project Structure
| File | Purpose |
|------|---------|
| `models.py`  | Classes: `Student`, `Exam`, `Result` |
| `records.py` | Add / display / find functions using ONE dictionary |
| `main.py`    | Menu-driven program |

## OOP Concepts Used
- **Classes & objects:** `Student`, `Exam`, `Result` (a `Result` links a Student object to an Exam object).
- **Instance methods:** `display_info()`, `update_record()`, `percentage()`, `grade()`, `status()`, `is_valid_score()`.
- **Class methods (`@classmethod`):** `Student.create_anonymous()`, `Exam.from_string()`.
- **Static methods (`@staticmethod`):** `Student.is_valid_id()`, `Result.calculate_grade()`.
- **Class attribute:** `Student._counter` (generates anonymous IDs).

## Data Structure
**One dictionary** stores all results.
Key = tuple `(student_id, exam_code)` (unique per result), Value = `Result` object.
**Tuples (bonus):** used as dictionary keys and for the grade boundaries `GRADE_BOUNDARIES`.

## Digital Public Goods (DPG) Alignment
| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | Hosted publicly on GitHub; uses only the Python standard library, so anyone can run, study and improve it. |
| **Inclusive & accessible** | Simple numbered menu, plain-language messages, clear error messages, input validation, no internet or special hardware needed (works on low-cost computers). |
| **Privacy-respecting** | Students are identified by anonymous IDs (e.g. `STU-001`) only. No names, addresses, phone numbers or other personal data are collected or stored. Data is kept in memory only. |
| **Modular & reusable** | Models, storage functions and the user interface are in separate files, so the classes can be reused in other school systems. |

## Sample Input / Output
```
Choose an option (1-6): 1
  Demo data loaded.
Choose an option (1-6): 3
STUDENT  | EXAM   | SUBJECT      | SCORE   | PERCENT | GRADE   | STATUS
------------------------------------------------------------------------------
STU-001  | E101   | Mathematics  |  85/100 |  85.0% | Grade A | PASS
STU-002  | E101   | Mathematics  |  62/100 |  62.0% | Grade C | PASS
STU-003  | E101   | Mathematics  |  41/100 |  41.0% | Grade F | FAIL
STU-001  | E102   | English      |  74/100 |  74.0% | Grade B | PASS
STU-002  | E102   | English      |  55/100 |  55.0% | Grade D | PASS
Choose an option (1-6): 5
  Exam code: E101
  Average for E101: 62.7%
Choose an option (1-6): 4
  Student ID: STU-003
  Exam code: E101
  New score: 55
  Updated:
STU-003  | E101   | Mathematics  |  55/100 |  55.0% | Grade D | PASS
```

## Grade Scale
A: 80+ | B: 70-79 | C: 60-69 | D: 50-59 | F: below 50

## Author
Ibrahim Sumaray (905005865) - Limkokwing University of Creative Technology, Sierra Leone
