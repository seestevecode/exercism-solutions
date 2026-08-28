"""Create a roster for a School"""

# pylint: disable=missing-function-docstring

class School:  # pylint: disable=missing-class-docstring
    def __init__(self):
        self._grades = {}
        self.add_list = []

    def add_student(self, name, grade):
        if name not in self.roster():
            self._grades[grade] = self._grades.get(grade, []) + [name]
            self.add_list.append(True)
        else:
            self.add_list.append(False)  

    def roster(self):
        return [
            name
            for grade in sorted(self._grades)
            for name in sorted(self._grades[grade])
        ]

    def grade(self, grade_number):
        return sorted(self._grades.get(grade_number, []))

    def added(self):
        return self.add_list
