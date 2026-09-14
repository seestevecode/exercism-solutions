"""Determine which plants a student is in charge of within a garden"""

# pylint: disable=missing-function-docstring

DEFAULT_STUDENTS = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
)

PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}


class Garden:  # pylint: disable=missing-class-docstring,too-few-public-methods
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self._garden = diagram.split('\n')
        self._students = sorted(students)

    def plants(self, student):
        student_index = self._students.index(student)
        return [
            PLANTS[plant]
            for row in self._garden 
            for plant in row[student_index * 2:student_index * 2 + 2]
        ]
