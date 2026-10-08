# Reviewed under SE2 coding standards guidelines
"""Student Grade Management System.

This module provides the Student class and demonstration utilities to manage
student records, compute grade statistics, determine academic standing,
and handle errors according to coding standard guidelines.
"""


class Student:
    """Represents a student and manages their academic records."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize a new Student record.

        Args:
            student_id: The unique identifier for the student.
            name: The full name of the student.
        """
        self.student_id = ""
        self.name = ""
        self.grades: list[float] = []

        if not isinstance(student_id, str) or not student_id.strip():
            print(
                f"Error: Invalid student ID '{student_id}'. "
                "Student ID cannot be empty."
            )
        else:
            self.student_id = student_id.strip()

        if not isinstance(name, str) or not name.strip():
            print(
                f"Error: Invalid student name '{name}'. "
                "Student name cannot be empty."
            )
        else:
            self.name = name.strip()

    def add_grade(self, grade: float) -> bool:
        """Add a numeric grade within the valid range [0, 100].

        Args:
            grade: Numeric grade value to add.

        Returns:
            bool: True if the grade was added successfully, False otherwise.
        """
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print(
                f"Error: Invalid grade '{grade}'. "
                "Grade must be a numeric value."
            )
            return False

        if not 0.0 <= float(grade) <= 100.0:
            print(
                f"Error: Invalid grade {grade}. "
                "Grade must be between 0 and 100."
            )
            return False

        self.grades.append(float(grade))
        return True

    def calculate_average(self) -> float:
        """Calculate the average grade of the student safely.

        Returns:
            float: The mean grade or 0.0 if no grades are recorded.
        """
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def get_letter_grade(self) -> str:
        """Convert the student's average grade into a letter grade.

        Returns:
            str: Letter grade (A, B, C, D, F) or 'N/A' if no grades exist.
        """
        if not self.grades:
            return "N/A"
        avg = self.calculate_average()
        if avg >= 90.0:
            return "A"
        if avg >= 80.0:
            return "B"
        if avg >= 70.0:
            return "C"
        if avg >= 60.0:
            return "D"
        return "F"

    def is_passed(self) -> bool:
        """Determine whether the student has passed.

        Returns:
            bool: True if the average is 60 or higher with grades, else False.
        """
        return bool(self.grades and self.calculate_average() >= 60.0)

    def get_status(self) -> str:
        """Return the passing status as a string.

        Returns:
            str: 'Passed' or 'Failed'.
        """
        return "Passed" if self.is_passed() else "Failed"

    def is_honor_roll(self) -> bool:
        """Determine if the student qualifies for the Honor Roll.

        Returns:
            bool: True if the average is 90 or higher with grades, else False.
        """
        return bool(self.grades and self.calculate_average() >= 90.0)

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove a grade by its zero-based position index.

        Args:
            index: The index of the grade to remove.

        Returns:
            bool: True if removed successfully, False if index is invalid.
        """
        if isinstance(index, bool) or not isinstance(index, int):
            print(
                f"Error: Invalid index '{index}'. Index must be an integer."
            )
            return False

        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(
                f"Grade {removed:.1f} at index {index} removed successfully."
            )
            return True

        print(
            f"Error: Index {index} is out of bounds for the grade list."
        )
        return False

    def remove_grade_by_value(self, grade: float) -> bool:
        """Remove the first occurrence of a grade matching the given value.

        Args:
            grade: Numeric grade value to remove.

        Returns:
            bool: True if removed successfully, False if not found.
        """
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print(
                f"Error: Invalid grade value '{grade}'. Must be a number."
            )
            return False

        target = float(grade)
        if target in self.grades:
            self.grades.remove(target)
            print(f"Grade {target:.1f} removed successfully.")
            return True

        print(f"Error: Grade value {target:.1f} not found in grade list.")
        return False

    def generate_report(self) -> str:
        """Generate a formatted academic summary report.

        Returns:
            str: Multi-line string with student academic details.
        """
        avg = self.calculate_average()
        avg_display = f"{avg:.2f}" if self.grades else "N/A"
        border = "-" * 42
        lines = [
            border,
            f"STUDENT SUMMARY REPORT: {self.name or 'UNKNOWN'}",
            border,
            f"Student ID       : {self.student_id or 'NOT ASSIGNED'}",
            f"Student Name     : {self.name or 'NOT ASSIGNED'}",
            f"Number of Grades : {len(self.grades)}",
            f"Average Grade    : {avg_display}",
            f"Letter Grade     : {self.get_letter_grade()}",
            f"Pass/Fail Status : {self.get_status()}",
            f"Honor Roll       : {self.is_honor_roll()}",
            border,
        ]
        return "\n".join(lines)

    def report(self) -> None:
        """Print the student summary report to standard output."""
        print(self.generate_report())


def demonstrate_validation() -> None:
    """Demonstrate handling of invalid student and grade inputs."""
    print("=== Testing Input Validation and Error Handling ===")
    Student("", "")
    Student("S001", "   ")

    sample = Student("STU01", "Test Student")
    sample.add_grade("Fifty")  # type: ignore
    sample.add_grade(-15.0)
    sample.add_grade(120.0)

    sample.remove_grade_by_index(5)
    sample.remove_grade_by_value(99.9)
    print()


def demonstrate_students() -> None:
    """Demonstrate core and extended requirements with valid students."""
    print("=== Demonstrating Student Management System ===")

    student_a = Student("STU101", "Andres Salinas")
    student_a.add_grade(95.0)
    student_a.add_grade(92.0)
    student_a.add_grade(98.0)
    student_a.report()
    print()

    student_b = Student("STU102", "Anthony Navarrete")
    student_b.add_grade(70.0)
    student_b.add_grade(85.0)
    student_b.add_grade(45.0)
    print(f"Initial average for Anthony: {student_b.calculate_average():.2f}")
    student_b.remove_grade_by_value(45.0)
    student_b.remove_grade_by_index(0)
    student_b.add_grade(88.0)
    student_b.report()
    print()

    student_c = Student("STU103", "Charlie Kirk")
    student_c.add_grade(52.0)
    student_c.add_grade(48.0)
    student_c.report()
    print()


def main() -> None:
    """Run system demonstrations without uncaught exceptions."""
    demonstrate_validation()
    demonstrate_students()


if __name__ == "__main__":
    main()
